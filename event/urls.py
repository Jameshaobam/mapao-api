from django.urls import path
from . import views
app_name = 'url'
urlpatterns = [
    path('<int:event_id>/going/',views.setGoing,name='setGoing'),
    path('all/',views.allEvents,name='allEvents'),
    path('add/',views.postEvent,name='postEvent'),
    path('<int:event_id>/update/',views.updateEvent,name='updateEvent'),
    path('<int:event_id>/delete/',views.deleteEvent,name='deleteEvent'),
    #event detail method is not yet defined
]