from .models import Note, User
from .serializers import NoteSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly, IsOwner

# Create your views here.

class NoteList(generics.ListCreateAPIView):
    """
    List all notes.
    """
    #queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
    
    

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