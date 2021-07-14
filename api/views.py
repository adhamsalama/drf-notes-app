#from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
#from django.views.decorators.csrf import csrf_exempt
from .models import Note
from .serializers import NoteSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def notes_list(request, format=None):
    if request.method == "GET":
        notes = Note.objects.all()
        print(notes)
        serializer = NoteSerializer(notes, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == "POST":
        #data = JSONParser().parse(request)
        #serializer = NoteSerializer(data=data)
        print("==========================================")
        print(request.data)
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            #return JsonResponse(serializer.errors, status=400)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def note_detail(request, pk, format=None):
    """
    Retrieve, update or delete a note.
    """
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        #return HttpResponse(status=404)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = NoteSerializer(note)
        #return JsonResponse(serializer.data)
        return Response(serializer.data)

    elif request.method == "PUT":
        #data = JSONParser().parse(request)
        #serializer = NoteSerializer(note, data=data)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return JsonResponse(serializer.data)
            return Response(serializer.data)

        else:
            #return JsonResponse(serializer.errors, status=400)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        note.delete()
        #return HttpResponse(status=204)
        return Response(status=status.HTTP_204_NO_CONTENT)