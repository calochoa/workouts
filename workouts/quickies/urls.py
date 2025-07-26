from django.urls import path
from . import views

# Define a list of url patterns
urlpatterns = [
    path('', views.home, name='quickies_home'),
    path('library/', views.library, name='quickies_library'),
    path('roulette/', views.roulette, name='quickies_roulette'),
]