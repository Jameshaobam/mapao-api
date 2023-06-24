# Generated by Django 4.2 on 2023-06-19 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0003_alter_profile_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=500)),
                ('origin_location', models.CharField(max_length=150)),
                ('based_location', models.CharField(max_length=150)),
                ('source_link', models.CharField(blank=True, max_length=300, null=True)),
                ('social_media_link', models.CharField(blank=True, max_length=300, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discover.category')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
            options={
                'verbose_name': 'Discover',
                'verbose_name_plural': 'Discoveries',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_description', models.CharField(max_length=1000)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('discover_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discover.discover')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discover_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discover.discover')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
