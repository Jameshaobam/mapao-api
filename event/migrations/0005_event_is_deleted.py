# Generated by Django 4.2 on 2023-07-01 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_alter_status_options_event_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_deleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
