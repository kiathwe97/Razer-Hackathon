from django.urls import path

from . import views

urlpatterns = [
    path("", views.open_account_view, name = "register"),
    #path("registersuccess/", views.creation_page, name = "registersuccess")
]
