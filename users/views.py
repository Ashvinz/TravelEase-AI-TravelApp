from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserDetailSerializer

# Create your views here.
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserMeView(generics.RetrieveAPIView): # Changed name for clarity
    serializer_class = UserDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user
