from django.urls import path
from .views import Area_List


urlpatterns = [

  path('', Area_List.as_view(), name='list_land')


]