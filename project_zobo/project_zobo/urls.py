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
from open_account.views import open_account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("demo.urls") ),
    path("page_2/", include("page_2.urls")),
    path("create_product/", product_create_view),
    path("OpenAccount/", open_account_view)
]
