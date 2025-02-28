from django.urls import path
from .import views

urlpatterns = [
    path('submit/', views.submit_data, name='submit_data'),
    path('view/', views.view_data, name='view_data')


]