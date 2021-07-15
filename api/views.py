from .models import Note, User
from .serializers import NoteSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.decorators import api_view
from rest_framework.respone import Response
from rest_framework.reverse import reverse

# Create your views here.

@apie_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format)
    })


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