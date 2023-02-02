from django.shortcuts import get_object_or_404
from .models import SocialCard, User
from .serializers import UserSerializer, SocialCardSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
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


class CardsList(ListCreateAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer
    permission_classes = [IsAuthenticated]


class MyCards(ListCreateAPIView):
    serializer_class = SocialCardSerializer

    def get_queryset(self):
        return SocialCard.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(RetrieveAPIView):
    serializer_class = SocialCardSerializer
    lookup_url_kwarg = 'card_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SocialCard.objects.all()


class CardEdit(RetrieveUpdateDestroyAPIView):
    serializer_class = SocialCardSerializer
    lookup_url_kwarg = 'card_id'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SocialCard.objects.filter(owner=self.request.user)

class CardSearch(ListAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("tags")
        if search_term is not None:
            return self.queryset.filter(tags__name__in=[search_term])