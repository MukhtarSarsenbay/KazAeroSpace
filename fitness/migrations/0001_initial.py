# Generated by Django 5.0.3 on 2024-04-02 17:34

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="GymRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("client", "Клиент"),
                            ("trainer", "Тренер"),
                            ("admin", "Админ"),
                        ],
                        default="client",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day_of_week", models.CharField(default="Monday", max_length=10)),
                ("start_time", models.TimeField(default="09:00")),
                ("end_time", models.TimeField(default="10:00")),
                (
                    "gym",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fitness.gymroom",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("time", models.TimeField(default="09:00")),
                (
                    "client",
                    models.ForeignKey(
                        limit_choices_to={"role": "client"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fitness.profile",
                    ),
                ),
                (
                    "schedule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fitness.schedule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trainer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Мужской"), ("female", "Женский")],
                        default="male",
                        max_length=10,
                    ),
                ),
                ("gyms", models.ManyToManyField(to="fitness.gymroom")),
                (
                    "user",
                    models.OneToOneField(
                        limit_choices_to={"role": "trainer"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fitness.profile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="schedule",
            name="trainer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fitness.trainer"
            ),
        ),
    ]
