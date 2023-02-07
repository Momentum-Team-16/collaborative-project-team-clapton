from django.shortcuts import get_object_or_404
from .models import SocialCard, User, Follower, Comments
from .serializers import UserSerializer, SocialCardSerializer, FollowerSerializer, CommentsSerializer, UserAvatarSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import parsers

# Create your views here.


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CardLike(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, card_id, format=None):
        card = get_object_or_404(SocialCard, id=card_id)
        user = self.request.user
        liked = False
        if card.likes.filter(username=user.username).exists():
            liked = False
            card.likes.remove(user)
        else:
            liked = True
            card.likes.add(user)

        data = {
            "liked": liked
        }

        return Response(data)


class CardsList(ListAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer


class MyCards(ListCreateAPIView):
    serializer_class = SocialCardSerializer

    def get_queryset(self):
        return SocialCard.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = SocialCardSerializer
    lookup_url_kwarg = 'card_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return SocialCard.objects.all()
        return SocialCard.objects.filter(owner=self.request.user)


class CardSearch(ListAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("tags")
        if search_term is not None:
            return self.queryset.filter(tags__name__in=[search_term])


class FollowerDetail(ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    lookup_url_kwarg = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follower.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user_to_follow = get_object_or_404(User, username=self.kwargs['username'])
        serializer.save(user=self.request.user, followed=user_to_follow)


class Unfollow(DestroyAPIView):
    serializer_class = FollowerSerializer
    lookup_field = 'followed'
    lookup_url_kwarg = 'username'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follower.objects.filter(user=self.request.user)
        return queryset

    def get_object(self):
        return self.request.user.LoggedInUser.filter(followed__username=self.kwargs[self.lookup_url_kwarg]).first()


class OtherUserCards(ListAPIView):
    serializer_class = SocialCardSerializer
    lookup_url_kwarg = 'username'

    def get_queryset(self):
        user_id = get_object_or_404(User, username=self.kwargs['username'])
        return SocialCard.objects.filter(owner=user_id)


class FollowedCards(ListAPIView):
    serializer_class = SocialCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        followed_list = self.request.user.followed_list
        return SocialCard.objects.filter(owner__in=followed_list)


class CommentsList(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

class UserAvatarCreateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAvatarSerializer
    parser_classes = [parsers.FileUploadParser]

    def get_object(self):
        return self.request.user
