from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ['content', 'date']