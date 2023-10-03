# Generated by Django 4.2 on 2023-06-29 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Status', 'verbose_name_plural': 'Statuses'},
        ),
        migrations.AddField(
            model_name='event',
            name='state',
            field=models.CharField(default='manipur', max_length=200),
            preserve_default=False,
        ),
    ]