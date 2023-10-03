# Generated by Django 4.0 on 2023-07-03 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_feed_feed_type'),
        ('account', '0003_alter_profile_id'),
        ('discover', '0003_like_liker'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscoverEditorChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('discover_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discover.discover')),
                ('feed_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.feed')),
            ],
        ),
    ]