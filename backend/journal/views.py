from rest_framework import viewsets
from rest_framework import permissions
from .models import Category, Journal
from .serializers import CategorySerializer, JournalSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsOwnerOrReadOnly]



