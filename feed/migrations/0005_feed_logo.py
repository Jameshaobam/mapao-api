# Generated by Django 4.0 on 2023-07-09 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_alter_feed_related_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='logo',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
