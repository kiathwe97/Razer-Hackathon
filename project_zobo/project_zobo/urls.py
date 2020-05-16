"""project_zobo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from page_2.views import product_create_view
from open_account.views import open_account_view, register_success_view
from login.views import login_view, verify_login_view, verify_login_singpass
from loan_status.views import loan_application, myinfo_message
from my_account.views import my_account_view, my_dashboard
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("demo.urls") ),
    path("page_2/", include("page_2.urls")),
    path("create_product/", product_create_view),
    path("register/", open_account_view),
    path("registersuccess/", register_success_view),
    path("login/", login_view),
    path("login/verifylogin/", verify_login_view),
    path("login/homepage", include("demo.urls")),
    path("login/verifylogin/verifyloginsingpass", verify_login_singpass),
    path("login/verifylogin/dashboard", my_dashboard),
    path("login/verifylogin/loanapplication", loan_application),
    path("login/verifylogin/myinfomessage", myinfo_message),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
