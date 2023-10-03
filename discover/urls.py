from django.urls import path
from . import views
app_name = 'discover'
urlpatterns = [
  
   #get all discoveries with Post/add discover included
    path('v1/discover/',views.getDiscovers,name='getDiscovers'),
    path('v1/categories/',views.getCategories,name='getCategories'),
    # path('v1/<int:cat_id>/categorized-discoveries/',views.getCategorizedDiscoveries,name='getCategorizedDiscoveries'),
    path('v1/categorized-discoveries/',views.getCategorizedDiscoveries,name='getCategorizedDiscoveries'),
    path('v1/discover/<int:disc_id>/',views.getDetailDiscover,name='getDetailDiscover'),
    path('v1/discover/<int:disc_id>/like/',views.likeDiscover,name='likeDiscover'),
    path('v1/discover/<int:disc_id>/delete/',views.deleteDiscover,name='deleteDiscover'),
    path('v1/discover/<int:disc_id>/add-review/',views.addReview,name='addReview'),
    path('v1/discover/<int:disc_id>/update/',views.updateDiscover,name='updateDiscover'),
    # to be added editor choice end point
    path('v1/discover/ec/<int:disc_id>/',views.makeEditorChoice,name='makeEditorChoice'),
    
    path('v1/discoveries/me/',views.getMyDiscoveries,name='getMyDiscoveries'),

]