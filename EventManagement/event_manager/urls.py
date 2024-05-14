from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for rendering views
    path('', views.home, name='home'),  # URL for the home page
    path('events/', views.events, name='events'),  # URL for the events page
    path('about/', views.about, name='about'),  # URL for the about page
    # Add more URL patterns for other views as needed
]
