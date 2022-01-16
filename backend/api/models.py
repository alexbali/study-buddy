from django.db import models


ROOM_TOPICS = {
    ("STUDY", "study"),
    ("MEET_NEW_PEOPLE", "meet new people"),
}

# Create your models here.
class Room(models.Model):
    sid                             = models.CharField(max_length=200, primary_key=True)
    account_sid                     = models.CharField(max_length=200)
    date_created                    = models.DateTimeField(auto_now_add=False)
    date_updated                    = models.DateTimeField(auto_now_add=False)
    status                          = models.CharField(max_length=50, default="")
    type_of_room                    = models.CharField(max_length=50, default="")
    enabled_turn                    = models.BooleanField(default=True)
    unique_name                     = models.CharField(max_length=100, default="")
    max_participants                = models.IntegerField()
    max_participant_duration        = models.IntegerField()
    max_concurrent_published_tracks = models.IntegerField()
    duration                        = models.IntegerField()
    status_callback_method          = models.CharField(max_length=20)
    status_callback                 = models.CharField(max_length=200, null=True, blank=True)
    record_participants_on_connect  = models.BooleanField(default=False)
    audio_only                      = models.BooleanField(default=False)
    media_region                    = models.CharField(max_length=100, default="")
    empty_room_time_out             = models.IntegerField()
    unused_room_timeout             = models.IntegerField()
    end_time                        = models.DateTimeField(auto_now_add=False)
    url                             = models.CharField(max_length=200, null=True, blank=True)
    participants                    = models.CharField(max_length=200)
    recordings                      = models.CharField(max_length=200)
    recording_rules                 = models.CharField(max_length=200)
    description                     = models.CharField(max_length=500)
    course_subject                  = models.CharField(max_length=100, null=True, blank=True)
    topic_of_room                   = models.CharField(max_length=50, choices=ROOM_TOPICS, default="STUDY")

class User(models.Model):
    email = models.EmailField(max_length=200, primary_key=True)
    token = models.CharField(max_length=300)
