from django.urls import path
from . import views
app_name = 'feed'
urlpatterns = [
    path('v1/all/',views.allFeeds,name='allFeeds'),
    path('v1/add/',views.addFeed,name='addFeed'),

]