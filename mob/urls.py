from django.urls import path
from.views import*
urlpatterns = [
    path("",home,name="home"),
    path("login/",login,name="login"),
    path("signup/",signup,name="signup"),
    path("receipt/",receipt,name="receipt"),
    path("viewreceipt/",viewreceipt,name="viewrec"),
    path("deletereceipt/<int:pk>",deletereceipt,name="deletereceipt")
]
    