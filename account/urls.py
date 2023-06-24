from django.urls import path
from . import views

urlpatterns = [
 
    path('register/',views.userRegister,name="userRegister"),


]