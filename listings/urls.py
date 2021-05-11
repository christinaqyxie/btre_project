from django.urls import path

from . import views
#  '' will go back to home, or in this case, just /listings 
   
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
] 