from rest_framework import serializers
from .models import Note, User

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'date', 'owner', 'tags']
    
    # Field-level validation
    # https://www.django-rest-framework.org/api-guide/serializers/#field-level-validation

    def validate_content(self, value):
        if "bad word" in value.lower():
            raise serializers.ValidationError("Behave yourself")
        return value

    # Object-level validation
    def validate(self, data):
        if 'bad word' in data['content'].lower():
            raise serializers.ValidationError('Behave yourself')
        return data




class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'notes', 'password']
    