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
from django.contrib.auth.mixins import LoginRequiredMixin
import json


class HomeView(TemplateView):
    template_name = 'home/index.html'


class SummaryView(LoginRequiredMixin, TemplateView):
    template_name = 'home/summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(username=self.request.user)
        
        daily_totals = Expense.objects.filter(user_profile=user_profile) \
                                       .values('date') \
                                       .annotate(total_amount=Sum('amount')) \
                                       .order_by('date')
        
        daily_expenses_data = [
            {'date': total['date'].strftime("%Y-%m-%d"), 'total_amount': float(total['total_amount'])} 
            for total in daily_totals
        ]
        
        context['daily_expenses_json'] = json.dumps(daily_expenses_data)
        return context