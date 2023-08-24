from django.urls import path
from .views import Area_List, Land_Detail


urlpatterns = [

  path('', Area_List.as_view(), name='list_land'),
  path('land_detail/<int:pk>', Land_Detail.as_view(), name='land_detail')


]