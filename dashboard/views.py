from django.shortcuts import render
from django.http import HttpRequest
import calendar
from client.models import Client
from authentication.models import ClientAuth
from datetime import datetime, timedelta

import pymongo



# Create your views here.
def index(request:HttpRequest):
    new_data = []
    new_labels = []
    try:
        client = Client.objects.get(name=request.user)
        lists = client.previous_balance
        for i in lists:
            new_data.append(i.get('figures'))
            new_labels.append(i.get('current_time').strftime('%H:%M:%S'))
    except:
        pass
    data = [1,2,3,4,5]
    labels = [calendar.month_name[i] for i in range(1, 8)]

    data = new_data
    labels = new_labels
    
    return render(request, 'index2.html', {'data':data, 'labels':labels})