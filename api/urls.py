from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "api"

urlpatterns = [
    path('notes', views.NoteList.as_view(), name='note-list'),
    path('notes/<int:pk>', views.NoteDetail.as_view()),
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('users/current_user', views.get_username, name="current-user"),
    path('', views.api_root),
    path('login', views.LoginUser.as_view(), name='login-user'),
    path('logout', views.LogoutUser.as_view(), name='logout-user'),
    path('register', views.RegisterUser.as_view(), name='register-user'),

]

urlpatterns = format_suffix_patterns(urlpatterns)