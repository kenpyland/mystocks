
from django.urls import path
from . import views


urlpatterns = [
  	path('', views.home, name="home"), 
  	path('about', views.about, name="about"),
  	path('add_mystocks', views.add_mystocks, name="add_mystocks"),
  	path('delete/<db_pkey>', views.delete, name="delete")

]
