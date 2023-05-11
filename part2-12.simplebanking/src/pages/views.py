from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json
from .forms import iban


@login_required
def addView(request):
    if request.method == "POST":
        form = iban(request.POST)
        if form.is_valid():
            new_account = form.cleaned_data['iban']
            add_account = Account.objects.create(owner = request.user, iban = new_account)
            add_account.save()
        
    return redirect('/')


@login_required
def homePageView(request):
    accounts = request.session.get('accounts')
    accounts = []
    try:
        users_accounts = Account.objects.filter(owner=request.user)
        print(users_accounts)
        for a in users_accounts:
            accounts.append(str(a))
    except:
        print("no accounts")
    request.session['accounts'] = accounts
    print(accounts)
    return render(request, 'pages/index.html', {'accounts' : accounts})


