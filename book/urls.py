from django.urls import path
from . import views

urlpatterns = [
    path('hi_link/', views.hi_view, name='hello'),
    path('book_link', views.book_viev, name='book'),
]