from django.shortcuts import render, redirect

# Create your views here.

def my_account_view(request):
    return render(request, "myaccount.html")

def my_dashboard(request):

    return render(request, "dashboard.html")

def my_account(request):
    return render(request, "myaccount.html")

def make_payment(request):
    return render(request, "makepayment.html")


def logout(request):
    return  redirect('/')

def login(request):
    return redirect('/login')
