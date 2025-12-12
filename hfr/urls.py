"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include 
from .views import home , about_us , amenities , contact_us , gallery , rooms, room_detail, booking 

urlpatterns = [
    path('', home, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('amenities/', amenities, name='amenities'),
    path('contact_us/', contact_us, name='contact_us'),
    path('gallery/', gallery, name='gallery'),
    path('rooms/', rooms, name='rooms'),
    path('room_detail/', room_detail, name='room_detail'),
    path('booking/', booking, name='booking'),

]
