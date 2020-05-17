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
from open_account.views import open_account_view, register_success_view, about_open_account, letter_offer, letter_signed, sign_letter, open_account_application
from login.views import login_view, verify_login_view, verify_login_singpass, verify_login_mobile
from loan_status.views import loan_application, myinfo_message, loan_app_complete, loan_submit, loan_status,about_loan, loan_approved
from my_account.views import my_account_view, my_dashboard, my_account, make_payment, logout, login
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
    path("login/verifylogin/loanappcomplete", loan_app_complete),
    path("login/verifylogin/loansubmit", loan_submit),
    path("login/verifylogin/loanstatus", loan_status),
    path("login/verifylogin/myaccount", my_account),
    path("login/verifylogin/makepayment", make_payment),
    path("register/registersuccess", register_success_view),
    path("register/verifylogin", verify_login_view),
    path("register/verifyloginsingpass", verify_login_singpass),
    path("register/verifyloginmobile", verify_login_mobile),
    path("register/dashboard", my_dashboard),
    path("register/loanapplication", loan_application),
    path("register/myinfomessage", myinfo_message),
    path("register/loanappcomplete", loan_app_complete),
    path("register/loansubmit", loan_submit),
    path("register/loanstatus", loan_status),
    path("register/myaccount", my_account),
    path("register/makepayment", make_payment),
    path("register/aboutopenaccount", about_open_account),
    path("register/openaccountapplication", open_account_application),
    path("register/aboutloan", about_loan),
    path("register/loanapproved", loan_approved),
    path("register/letteroffer", letter_offer),
    path("register/lettersigned", letter_signed),
    path("register/signletter", sign_letter),
    path("register/homepage", logout),
    path("register/login", login),
    
    
    path("login/verifylogin/registersuccess", register_success_view),
    path("login/verifylogin/verifylogin", verify_login_view),
    path("login/verifylogin/verifyloginsingpass", verify_login_singpass),
    path("login/verifylogin/verifyloginmobile", verify_login_mobile),
    path("login/verifylogin/dashboard", my_dashboard),
    path("login/verifylogin/loanapplication", loan_application),
    path("login/verifylogin/myinfomessage", myinfo_message),
    path("login/verifylogin/loanappcomplete", loan_app_complete),
    path("login/verifylogin/loansubmit", loan_submit),
    path("login/verifylogin/loanstatus", loan_status),
    path("login/verifylogin/myaccount", my_account),
    path("login/verifylogin/makepayment", make_payment),
    path("login/verifylogin/aboutopenaccount", about_open_account),
    path("login/verifylogin/openaccountapplication", open_account_application),
    path("login/verifylogin/aboutloan", about_loan),
    path("login/verifylogin/loanapproved", loan_approved),
    path("login/verifylogin/letteroffer", letter_offer),
    path("login/verifylogin/lettersigned", letter_signed),
    path("login/verifylogin/signletter", sign_letter),
    path("login/verifylogin/homepage", logout),
    path("login/verifylogin/login", login),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
