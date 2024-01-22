from django.urls import path
from .views import HomeView, SummaryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('summary/', SummaryView.as_view(), name='summary'),
    # other paths
]