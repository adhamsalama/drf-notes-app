from .models import Note, User
from .serializers import NoteSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import UserRateThrottle
from .throttlers import PostUserRateThrottle
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from rest_framework.views import APIView


# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('api:user-list', request=request, format=format),
        'notes': reverse('api:note-list', request=request, format=format)
    })

#@action(detail=True, methods=["post"], throttle_classes=[PostUserRateThrottle])
class NoteList(generics.ListCreateAPIView):
    """
    List all notes.
    """
    #queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [PostUserRateThrottle]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-date')
    
    

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a note."
    """
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterUser(APIView):
    def post(self, request):
        print(request.data)
        user = User.objects.create_user(username=request.data['username'], password=request.data['password'])
        user.save()
        login(request, user)
        return Response({"Registered successfully."}, status=200)


class LoginUser(APIView):
    def post(self, request):
        print(request.data)
        user = authenticate(request, username=request.data['username'], password=request.data['password'])
        print(user)
        if user is not None:
            login(request, user)
            return Response({"Logged in successfully."}, status=200)
        else:
            return Response({"Invalid credentials."}, status=400)


class LogoutUser(APIView):
    def get(self, request):
        logout(request)
        return Response({"Logged out successfully."},status=200)


@api_view(["GET"])
def get_username(request):
    return Response({
        'username': request.user.username
    })
