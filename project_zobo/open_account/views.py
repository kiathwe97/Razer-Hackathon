from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.

def open_account_view(request):

    return render(request, 'OpenAccount.html')

