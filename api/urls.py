from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('notes', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>', views.NoteDetail.as_view()),
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('', views.api_root)
]

urlpatterns = format_suffix_patterns(urlpatterns)