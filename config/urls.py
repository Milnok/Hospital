"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api.views import NoteList, CheckLogin, DeleteNote, UpdateNote, NoteById, CreateNode
from frontend.views import IndexView, LoginView, DetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),

    path('api/v1/get_nodes', NoteList.as_view()),
    path('api/v1/get_node_by_id', NoteById.as_view()),
    path('api/v1/check_login', CheckLogin.as_view()),
    path('api/v1/create_node', CreateNode.as_view()),
    path('api/v1/delete_node/<int:id>', DeleteNote.as_view()),
    path('api/v1/update_note/<int:id>', UpdateNote.as_view()),

    path('', IndexView.as_view()),
    path('login/', LoginView.as_view()),
    path('detail/', DetailView.as_view()),
]
