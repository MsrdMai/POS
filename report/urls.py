from django.contrib import auth
from django.urls import path

from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('day_dashboard/', views.day_dashboard, name='day_dashboard'),
    path('week_dashboard/', views.week_dashboard, name='week_dashboard'),
    path('month_dashboard/', views.month_dashboard, name='month_dashboard'),
    path('year_dashboard/', views.year_dashboard, name='year_dashboard'),

]