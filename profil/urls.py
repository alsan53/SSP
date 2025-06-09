from django.urls import path
from . import views

urlpatterns = [
    path('omah/', views.home),
    path('berita/', views.berita),
    path('tentang/', views.about),
    path('harga/', views.price),
]