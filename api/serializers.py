from rest_framework import serializers
from api.models import Note, Doctor, Patient, Timetable


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('first_name', 'last_name',)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name',)


class NoteSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()

    class Meta:
        model = Note
        fields = ('doctor', 'patient', 'description', 'id')


class TimeTableSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = Timetable
        fields = '__all__'
        extra_kwargs = {'monday_start': {'format': '%H:%M'},
                        'monday_end': {'format': '%H:%M'},
                        'tuesday_start': {'format': '%H:%M'},
                        'tuesday_end': {'format': '%H:%M'},
                        'wednesday_start': {'format': '%H:%M'},
                        'wednesday_end': {'format': '%H:%M'},
                        'thursday_start': {'format': '%H:%M'},
                        'thursday_end': {'format': '%H:%M'},
                        'friday_start': {'format': '%H:%M'},
                        'friday_end': {'format': '%H:%M'}}
