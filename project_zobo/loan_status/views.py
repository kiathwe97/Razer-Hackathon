from django.shortcuts import render

# Create your views here.

def loan_application(request):
    return render(request, "loanapplication.html")

def myinfo_message(request):
    return render(request, "myinfomessage.html")

def loan_app_complete(request):
    return render(request, "loanappcomplete.html")

def loan_submit(request):
    return render(request, "loansubmit.html")

def loan_status(request):
    return render(request, "loanstatus.html")

def about_loan(request):
    return render(request, "aboutloan.html")

def loan_approved(request):
    return render(request, "loanapproved.html")

