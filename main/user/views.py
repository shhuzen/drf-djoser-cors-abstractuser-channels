from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework import generics, viewsets, filters, status
from .pagination import VeryLargePagination
from rest_framework.response import Response

User = get_user_model()

class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = VeryLargePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
