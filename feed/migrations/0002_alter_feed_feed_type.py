# Generated by Django 4.0 on 2023-07-02 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='feed_type',
            field=models.CharField(choices=[('D', 'Discover'), ('E', 'Event'), ('U', 'Untold'), ('F', 'Feed')], default='F', max_length=1),
        ),
    ]