from .models import Profile, Trainer, GymRoom, Schedule, Appointment
from .serializers import ProfileSerializer, TrainerSerializer, GymRoomSerializer, ScheduleSerializer, AppointmentSerializer
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class GymRoomViewSet(viewsets.ModelViewSet):
    queryset = GymRoom.objects.all()
    serializer_class = GymRoomSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

