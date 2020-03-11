
from django.template.context_processors import request
from django.contrib.auth.decorators import login_required, permission_required
from management.models import Order
from django.shortcuts import redirect, render
from datetime import datetime, timedelta

from django.utils.timezone import datetime
from django.utils import formats
# Create your views here.
@login_required
@permission_required('management.adjustlist')
def dashboard(request):
    return render(request, 'report/report.html')


def day_dashboard(request):
    now = datetime.now()
    day = now.strftime('%d')
    total_day = Order.objects.filter(date_time__day=day)
    profit = 0
    for i in total_day:
        profit += i.total_price
    context = {
        'total_day' : total_day,
        'profit' : profit,
    }
    return render(request, 'report/day.html', context=context)


   
def month_dashboard(request):
    now = datetime.now()
    month = now.strftime('%m')
    total_month = Order.objects.filter(date_time__month=month)
    profit = 0
    for i in total_month:
        profit += i.total_price
    context = {
        'total_month' : total_month,
        'profit' : profit,
    }
    return render(request, 'report/month.html', context=context)
    
    

def year_dashboard(request):
    now = datetime.now()
    year = now.strftime('%Y')
    total_year = Order.objects.filter(date_time__year=year)
    profit = 0
    for i in total_year:
        profit += i.total_price
    context = {
        'total_year' : total_year,
        'profit' : profit,
    }
    return render(request, 'report/year.html', context=context)
    
def week_dashboard(request):
    # now = datetime.now()
    # week = now.strftime('%W')
    # total_week = Order.objects.filter(date_time__week=52)
    # You can create a datetime for one week ago, then filter all jobs after that.
    one_week_ago = datetime.today() - timedelta(days=7)
    total_week = Order.objects.filter(date_time__gte=one_week_ago)

    profit = 0
    for i in total_week:
        profit += i.total_price
    context = {
        'total_week' : total_week,
        'profit' : profit,
    }
    return render(request, 'report/week.html', context=context)
    