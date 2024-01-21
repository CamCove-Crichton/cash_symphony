from django.views.generic import TemplateView, View
from django.shortcuts import render
from datetime import datetime
import calendar
from decimal import Decimal


class Index(TemplateView):
    template_name = 'home/index.html'
