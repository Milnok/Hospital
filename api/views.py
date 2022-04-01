from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from api.models import Note, Doctor, Patient
from api.serializers import NoteSerializer, CreateNoteSerializer


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


class CreateNote(CreateAPIView):
    serializer_class = CreateNoteSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        data = serializer.data
        print(data)
        try:
            patient = Patient.objects.get(first_name=data['first_name'],
                                          last_name=data['last_name'])
        except Patient.DoesNotExist:
            return Response('Patient', status=status.HTTP_404_NOT_FOUND)
        try:
            doctor = Doctor.objects.get(first_name=data['first_name'],
                                        last_name=data['last_name'])
        except Doctor.DoesNotExist:
            return Response('Doctor', status=status.HTTP_404_NOT_FOUND)
        Note.objects.create(doctor=doctor.id, patient=patient.id, description=data['description'])

        return Response(status=status.HTTP_204_NO_CONTENT)
