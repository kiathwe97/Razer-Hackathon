from django.shortcuts import render

# Create your views here.

def loan_application(request):
    return render(request, "loanapplication.html")

def myinfo_message(request):
    return render(request, "myinfomessage.html")
