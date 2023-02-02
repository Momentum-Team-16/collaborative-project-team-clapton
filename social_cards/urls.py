from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='profile'),
    path('cards/', views.CardsList.as_view(), name='cards'),
    path('cards/me/', views.MyCards.as_view(), name='my-cards'),
    path('cards/<int:card_id>/', views.CardDetail.as_view(), name='card-detail'),
    path('cards/<int:card_id>/edit', views.CardEdit.as_view(), name='card-edit'),
    path('search', views.CardSearch.as_view(), name='tags_search'),
]
