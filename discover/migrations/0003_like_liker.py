# Generated by Django 4.2 on 2023-07-01 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_profile_id'),
        ('discover', '0002_review_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='liker',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.profile'),
            preserve_default=False,
        ),
    ]
