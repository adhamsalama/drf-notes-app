from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('notes', views.notes_list),
    path('notes/<int:pk>', views.note_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)