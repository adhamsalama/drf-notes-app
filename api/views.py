from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics

# Create your views here.

class NotesList(generics.ListCreateAPIView):
    """
    List all notes.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a note."
    """
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
