from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tracker.models import Expense
from profiles.models import UserProfile
from django.db.models import Sum
from collections import defaultdict
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from datetime import date
from django.http import JsonResponse


class Index(TemplateView):
    template_name = 'home/index.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Index, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(username=self.request.user)
        
        # Calculate the total amount per day
        daily_totals = Expense.objects.filter(user_profile=user_profile) \
                                       .values('date') \
                                       .annotate(total_amount=Sum('amount')) \
                                       .order_by('date')
        
        # Convert QuerySet to list of dicts
        daily_expenses_data = [
            {'date': total['date'].strftime("%Y-%m-%d"), 'total_amount': float(total['total_amount'])} 
            for total in daily_totals
        ]
        
        # # Convert QuerySet to list of dicts
        # context['daily_expenses'] = [
        #     {'date': total['date'], 'total_amount': float(total['total_amount'])} 
        #     for total in daily_totals
        # ]
        context['daily_expenses_json'] = JsonResponse(list(daily_expenses_data), safe=False).content.decode()
        return context
