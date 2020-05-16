from django.shortcuts import render

# Create your views here.

def my_account_view(request):
    return render(request, "myaccount.html")

def my_dashboard(request):

    return render(request, "dashboard.html")
