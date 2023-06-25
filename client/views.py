from django.shortcuts import render, redirect
from django.http import HttpRequest
import decimal
from client.structure import data_convert
from django.utils import timezone
from .models import Client, Trade

# Create your views here.
def index(request:HttpRequest):
    pass

def trade(request:HttpRequest):
    initial_balance = decimal.Decimal(100.00)
    try:
        client = Client.objects.get(name=request.user)
        profit_loss = client.generate_profit_loss()
        current_balance = client.current_balance
        new_balance = data_convert(current_balance, profit_loss)
        client.current_balance = new_balance
        fresh_trade = Trade.objects.create(figures=decimal.Decimal(new_balance))
        new_trade = {'id':fresh_trade.id, 'figures':fresh_trade.figures, 'current_time': fresh_trade.current_time}
        client.previous_balance.append(new_trade)
        client.save()
    except:
        new_trade = Trade.objects.create(figures=initial_balance, current_time=timezone.now())
        Client.objects.create(name=request.user, initial_balance=initial_balance, current_balance=initial_balance, previous_balance=[{'id':new_trade.id, 'figures':new_trade.figures, 'current_time': new_trade.current_time}])
        
    return redirect('/')

