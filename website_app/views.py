from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    title_name = 'Python & Django'
    return render(request, 'pages/base.html',{
        'date': now,
        'year': year,
        'title_name': title_name,
    })
