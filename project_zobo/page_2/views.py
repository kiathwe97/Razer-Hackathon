from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.
from.models import Product
from .forms import ProductForm

def index(request):

    return render(request, 'page_2.html')

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product_form.html", context)

