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
        if value.lower() == "bad word":
            raise serializers.ValidationError("Not valid")
        return value

    # Object-level validation
    def validate(self, data):
        if data['content'].lower() == 'bad word':
            raise serializers.ValidationError('Not valid')
        return data




class UserSerializer(serializers.HyperlinkedModelSerializer):
    #notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'notes']