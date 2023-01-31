from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='profile'),
    path('cards/', views.CardsList.as_view(), name='cards'),
]