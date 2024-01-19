from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_budget, name='view_budget')
]