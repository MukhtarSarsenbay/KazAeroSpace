from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = (
        ('client', 'Клиент'),
        ('trainer', 'Тренер'),
        ('admin', 'Админ'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.user.username

class GymRoom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def validate_date_of_birth(value):
    if value > timezone.now().date():
        raise ValidationError("Дата рождения не может быть в будущем.")
class Trainer(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, limit_choices_to={'role': 'trainer'})
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(validators=[validate_date_of_birth])
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский')], default='male')
    gyms = models.ManyToManyField(GymRoom, related_name='trainers')
    def save(self, *args, **kwargs):
        if self.user.role != 'trainer':
            raise ValueError("A Trainer must have a Profile with the role of 'trainer'")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

class Schedule(models.Model):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAY_OF_WEEK_CHOICES = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    day_of_week = models.CharField(
        max_length=10,
        choices=DAY_OF_WEEK_CHOICES,
        default=MONDAY,
    )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    gym = models.ForeignKey(GymRoom, on_delete=models.CASCADE)
    start_time = models.TimeField(default='09:00')
    end_time = models.TimeField(default='10:00')

    def __str__(self):
        return f"{self.trainer.full_name} - {self.gym.name} - {self.day_of_week}"

class Appointment(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, limit_choices_to={'role': 'client'})
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default='09:00')

    def __str__(self):
        return f"{self.schedule.trainer.full_name} - {self.client.user.username} - {self.date}"

