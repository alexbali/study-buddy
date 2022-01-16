# Generated by Django 3.2.11 on 2022-01-16 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('sid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('account_sid', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('status', models.CharField(default='', max_length=50)),
                ('type_of_room', models.CharField(default='', max_length=50)),
                ('enabled_turn', models.BooleanField(default=True)),
                ('unique_name', models.CharField(default='', max_length=100)),
                ('max_participants', models.IntegerField()),
                ('max_participant_duration', models.IntegerField()),
                ('max_concurrent_published_tracks', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('status_callback_method', models.CharField(max_length=20)),
                ('status_callback', models.CharField(blank=True, max_length=200, null=True)),
                ('record_participants_on_connect', models.BooleanField(default=False)),
                ('audio_only', models.BooleanField(default=False)),
                ('media_region', models.CharField(default='', max_length=100)),
                ('empty_room_time_out', models.IntegerField()),
                ('unused_room_timeout', models.IntegerField()),
                ('end_time', models.DateTimeField()),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('participants', models.CharField(max_length=200)),
                ('recordings', models.CharField(max_length=200)),
                ('recording_rules', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('course_subject', models.CharField(blank=True, max_length=100, null=True)),
                ('topic_of_room', models.CharField(choices=[('STUDY', 'study'), ('MEET_NEW_PEOPLE', 'meet new people')], default='STUDY', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=200, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=300)),
            ],
        ),
    ]
