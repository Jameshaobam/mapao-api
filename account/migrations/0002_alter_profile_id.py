# Generated by Django 4.2 on 2023-06-19 13:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0fa7d4b0-3048-454c-ae97-3e18d876cfe1'), primary_key=True, serialize=False, unique=True),
        ),
    ]
