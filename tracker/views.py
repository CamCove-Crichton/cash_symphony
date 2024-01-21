from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense
from .forms import ExpenseForm
from profiles.models import UserProfile
from collections import defaultdict
from django.db.models import Sum



@login_required
def list_expenses(request):
    user_profile = UserProfile.objects.get(username=request.user)
    expenses_list = Expense.objects.filter(user_profile=user_profile).order_by('-date')
    expenses_grouped = defaultdict(list)
    
    # Calculate the total amount per day
    daily_totals = Expense.objects.filter(user_profile=user_profile) \
                                   .values('date') \
                                   .annotate(total_amount=Sum('amount')) \
                                   .order_by('-date')
    
    daily_totals_dict = {total['date']: total['total_amount'] for total in daily_totals}

    for expense in expenses_list:
        expenses_grouped[expense.date].append(expense)

    context = {
        'expenses_grouped': dict(expenses_grouped),
        'daily_totals': daily_totals_dict
    }
    return render(request, 'tracker/list_expense.html', context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            
            # Retrieve the UserProfile instance associated with the current user
            user_profile = UserProfile.objects.get(username=request.user)  # Adjust to the correct field name
            
            expense.user_profile = user_profile  # Assign the UserProfile instance
            expense.save()
            
            return redirect('list_expenses')  # Redirect to the list of expenses after adding
    else:
        form = ExpenseForm()
    return render(request, 'tracker/add_expense.html', {'form': form})





@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user_profile=UserProfile.objects.get(username=request.user))
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('list_expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'tracker/edit_expense.html', {'form': form})



@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user_profile=UserProfile.objects.get(username=request.user))
    if request.method == 'POST':
        expense.delete()
        return redirect('list_expenses')
    return render(request, 'tracker/delete_expense.html', {'expense': expense})
