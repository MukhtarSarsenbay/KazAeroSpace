from rest_framework import serializers
from .models import Profile, Trainer, GymRoom, Schedule, Appointment


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class GymRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymRoom
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['schedule', 'client', 'date', 'time']

    def validate(self, data):

        schedule = data.get('schedule')
        appointment_date = data.get('date')
        appointment_time = data.get('time')

        if schedule.day_of_week != appointment_date.strftime('%A'):
            raise serializers.ValidationError("Тренер не работает в этот день недели.")

        if not (schedule.start_time <= appointment_time <= schedule.end_time):
            raise serializers.ValidationError("Время записи вне рабочего времени тренера.")

        return data

