from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from api.models import Note, Doctor, Patient, Audit, Timetable
from api.serializers import NoteSerializer, TimeTableSerializer


class CheckLogin(ListAPIView):
    def get(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return JsonResponse({'login': None})
        if not self.request.user.is_anonymous:
            try:
                Patient.objects.get(username=self.request.user.username)
                return JsonResponse(
                    {'login_first': self.request.user.first_name, 'login_last': self.request.user.last_name,
                     'type': 'Patient'})
            except Patient.DoesNotExist:
                return JsonResponse(
                    {'login_first': self.request.user.first_name, 'login_last': self.request.user.last_name,
                     'type': 'Doctor'})


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
            return None

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        Audit.objects.create(user=self.request.user.username, table='Note', action='Удаление')
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateNote(UpdateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if Note.objects.filter(doctor=self.request.user.id):
            return Note.objects.all()
        else:
            return None

    def partial_update(self, request, *args, **kwargs):
        ret = super(UpdateAPIView, self).partial_update(request, *args, **kwargs)
        Audit.objects.create(user=self.request.user.username, table='Note', action='Удаление')
        return ret


class CreateNote(CreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            Doctor.objects.get(username=self.request.user.username)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        try:
            patient = Patient.objects.get(first_name=data['patient']['first_name'],
                                          last_name=data['patient']['last_name'])
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            doctor = Doctor.objects.get(first_name=data['doctor']['first_name'],
                                        last_name=data['doctor']['last_name'])
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        Note.objects.create(doctor=doctor, patient=patient, description=data['description'])
        Audit.objects.create(user=self.request.user.username, table='Note', action='Создание')
        return Response(status=status.HTTP_204_NO_CONTENT)


class TimeTableList(ListAPIView):
    serializer_class = TimeTableSerializer
    queryset = Timetable.objects.all()

