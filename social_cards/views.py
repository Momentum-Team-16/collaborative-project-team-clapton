from django.shortcuts import get_object_or_404
from .models import SocialCard, User, Follower
from .serializers import UserSerializer, SocialCardSerializer, FollowerSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated

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


class CardsList(ListAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer
    permission_classes = [IsAuthenticated]


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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Follower.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowerEdit(RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [IsAuthenticated]


class OtherUserCards(ListAPIView):
    serializer_class = SocialCardSerializer
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        user_id = get_object_or_404(User, id=self.kwargs['user_id'])
        return SocialCard.objects.filter(owner=user_id)


class FollowedCards(ListAPIView):
    serializer_class = SocialCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        followed_list = self.request.user.followed_list
        return SocialCard.objects.filter(owner__in=followed_list)
