from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    year = now.strftime("%Y")
    title_name = 'Python & Django'
    return render(request, 'pages/index.html',{
        'date': now,
        'year': year,
        'title_name': title_name,
    })
