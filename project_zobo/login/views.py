from django.shortcuts import render

# Create your views here.
def login_view(request):

    return render(request, "login.html")

def verify_login_view(request):

    return render(request, "verifylogin.html")

def verify_login_singpass(request):

    return render(request, "verifyloginsingpass.html")
