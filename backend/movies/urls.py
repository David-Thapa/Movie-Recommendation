from django.urls import path
from . import views

urlpatterns = [
    path('', views.movies_data),
    path('<int:id>/', views.movie_detail),
]