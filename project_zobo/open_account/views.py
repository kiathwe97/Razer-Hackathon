from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.
def open_account_view(request):

    return render(request, 'register.html')


def register_success_view(request):

    return render(request, "registersuccess.html")


def about_open_account(request):
    return render(request, "aboutopenaccount.html")

def letter_offer(request):
    return render(request, "letteroffer.html")

def letter_signed(request):
    return render(request, "lettersigned.html")

def sign_letter(request):
    return render(request, "signletter.html")

def open_account_application(request):
    return render(request, "openaccountapplication.html")



