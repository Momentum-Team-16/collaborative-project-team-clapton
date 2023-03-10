from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserView.as_view(), name='profile'),
    path('cards/', views.CardsList.as_view(), name='cards'),
    path('cards/me/', views.MyCards.as_view(), name='my_cards'),
    path('cards/followed/', views.FollowedCards.as_view(), name='followed_cards'),
    path('cards/<int:card_id>/', views.CardDetail.as_view(), name='card_detail'),
    path('cards/<username>/', views.OtherUserCards.as_view(), name='other_user_cards'),
    path('follower/<username>/', views.FollowerDetail.as_view(), name='follower_list'),
    path('unfollow/<username>/', views.Unfollow.as_view(), name='unfollow'),
    path('search', views.CardSearch.as_view(), name='tags_search'),
    path('comment/', views.CommentsList.as_view(), name='comments_list'),
    path('comment/<int:pk>/', views.CommentsDetail.as_view(), name='comments_detail'),
    path('like/<int:card_id>/', views.CardLike.as_view(), name='like'),
    path('users/me/avatar/', views.UserAvatarCreateView.as_view(), name='user_avatar'),
]
