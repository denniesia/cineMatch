from django.urls import path, include
from .views import index, movies_view

urlpatterns = [
    path('', index, name='index'),
    path('movies/', movies_view, name='movies'),
]