from django.contrib import admin
from django.urls import path

from . import views 


urlpatterns = [
    path('',views.index,name='index'),
    path('get_location_data/',views.get_location_data,name='get_location_data'),

]