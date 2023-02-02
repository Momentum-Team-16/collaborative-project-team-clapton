from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='profile'),
    path('cards/', views.CardsList.as_view(), name='cards'),
    path('cards/me/', views.MyCards.as_view(), name='my_cards'),
    path('cards/<int:card_id>/', views.CardDetail.as_view(), name='card_detail'),
    path('cards/<int:card_id>/edit/', views.CardEdit.as_view(), name='card_edit'),
    path('follower/', views.FollowerDetail.as_view(), name='follower_list'),
    path('follower/<int:pk>/', views.FollowerEdit.as_view(), name='follower_edit'),
    path('search', views.CardSearch.as_view(), name='tags_search'),
]
