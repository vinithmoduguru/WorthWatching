# Generated by Django 4.1.1 on 2022-09-07 15:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("name", models.CharField(max_length=100)),
                (
                    "rating",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        default=0.0,
                        max_digits=2,
                        null=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
