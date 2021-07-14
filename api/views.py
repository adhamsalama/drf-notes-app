from .models import Note
from .serializers import NoteSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.

class NotesList(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.CreateModelMixin):
    """
    List all notes.
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NoteDetail(generics.GenericAPIView,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin):
    """
    Retrieve, update or delete a note."
    """
    
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)