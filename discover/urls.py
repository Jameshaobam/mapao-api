from django.urls import path
from . import views

urlpatterns = [
 
    path('v1/discover',views.getDiscovers,name='getDiscovers'),
    path('v1/categories',views.getCategories,name='getCategories'),
    path('v1/<int:cat_id>/categorized-discoveries',views.getCategorizedDiscoveries,name='getCategorizedDiscoveries'),
    path('v1/discover/<int:disc_id>',views.getDetailDiscover,name='getDetailDiscover'),
    path('v1/discover/<int:disc_id>/like',views.likeDiscover,name='likeDiscover'),
    path('v1/discover/<int:disc_id>/delete',views.deleteDiscover,name='deleteDiscover'),

]