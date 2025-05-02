from django.urls import path, include
from .views import dashboard, index, movies_view

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('movies/', movies_view, name='movies'),
]