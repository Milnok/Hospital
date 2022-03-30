from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from api.models import Note, Doctor, Patient
from api.serializers import NoteSerializer


class CheckLogin(ListAPIView):
    def post(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return JsonResponse({'login': None})
        if not self.request.user.is_anonymous:
            try:
                Patient.objects.get(username=self.request.user.username)
                return JsonResponse({'login': self.request.user.username, 'type': 'Patient'})
            except Patient.DoesNotExist:
                return JsonResponse({'login': self.request.user.username, 'type': 'Doctor'})


class NoteList(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if Note.objects.filter(doctor=self.request.user.id):
            return Note.objects.filter(active=True)
        else:
            return Note.objects.filter(patient=self.request.user.id, active=True)


class NoteById(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if Note.objects.filter(doctor=self.request.user.id):
            return Note.objects.filter(active=True, id=self.request.GET['id'])
        else:
            return Note.objects.filter(patient=self.request.user.id, id=self.request.GET['id'], active=True)


class DeleteNote(DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if Note.objects.filter(doctor=self.request.user.id):
            return Note.objects.all()
        else:
            return Note.objects.filter(patient=self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateNote(UpdateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if Note.objects.filter(doctor=self.request.user.id):
            return Note.objects.all()
        else:
            return Note.objects.filter(patient=self.request.user.id)


class CreateNode(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
