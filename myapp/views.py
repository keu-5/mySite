from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index_template(request):
    myapp_data = {
        'app': 'Django',
        'num': range(10),
        'is_weekday': True,
    }
    return render(request, 'index.html', myapp_data)