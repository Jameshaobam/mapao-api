from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
 
    path('register/',views.userRegister,name="userRegister"),
    path('isauth/',views.isAuth,name="isAuth"),
    path('login/',views.userLogin,name="userLogin"),


]