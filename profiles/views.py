from django.shortcuts import render

# Create your views here.
def profile(request):
    """
    A view to render the users budget
    """
    context = {

    }
    template = 'profiles/profile.html'

    return render(request, template, context)