from django.shortcuts import render
from twilio.rest import Client

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.conf import settings
from twilio.jwt.access_token import AccessToken, grants
from django.views.decorators.csrf import csrf_exempt
from .models import Room, User
import json

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {})

class RoomView(View):
    def get(self, request, *args, **kwargs):
        rooms = client.video.rooms.list()

        rooms_reps = [
            {
                "room_name": conference.unique_name,
                "sid": conference.sid,
                "max_participants": conference.max_participants,
                "status": conference.status,
            } for conference in rooms]

        return JsonResponse({"rooms": rooms_reps})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        # create a new room 
        room_name = request.POST.get("room_name")
        max_participants = request.POST.get("max_participants")
        description = request.POST.get("description")
        course_subject = request.POST.get("course_subject")
        topic_of_room = request.POST.get("topic_of_room")
        room = client.video.rooms.create(
            unique_name=room_name,
            type="group",
            max_participants=max_participants,
        )
        createdRoom = Room.objects.create(
            sid: room.sid,
            account_sid: room.account_sid,
            date_created: room.date_created,
            date_updated: room.date_updated,
            status: room.status,
            type_of_room: room.type,
            enabled_turn: room.enabled_turn,
            unique_name: room.unique_name,
            max_participants: room.max_participants,
            max_participant_duration: room.max_participant_duration,
            max_concurrent_published_tracks: room.max_concurrent_published_tracks,
            duration: room.duration,
            status_callback_method: room.status_callback_method,
            status_callback: room.status_callback,
            record_participants_on_connect: room.record_participants_on_connect,
            audio_only: room.audio_only,
            media_region: room.media_region,
            empty_room_time_out: room.empty_room_time_out,
            unused_room_timeout: room.unused_room_timeout,
            end_time: room.end_time,
            url: room.url,
            participants: room.participants,
            recordings: room.recordings,
            recording_rules: room.recording_rules,
            description: description,
            course_subject: course_subject,
            topic_of_room: topic_of_room
        )
        createdRoom.save()
        return JsonResponse({"room_sid": room.sid})

class TokenView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data["username"]
        room_sid = data["sid"]

        if room_sid=='':
            video_grant = grants.VideoGrant(room='My Room')
        else:
            video_grant = grants.VideoGrant(room=room_sid)

        access_token = AccessToken(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_API_KEY,
            settings.TWILIO_API_SECRET,
            identity=username
        )

        access_token.add_grant(video_grant)

        jwt_token = access_token.to_jwt()
        print(jwt_token)
        return JsonResponse({"token": jwt_token})

    def get(self, request, username, *args, **kwargs):
        voice_grant = grants.VoiceGrant(
            outgoing_application_sid=settings.TWIML_APPLICATION_SID,
            incoming_allow=True,
        )
        access_token = AccessToken(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_API_KEY,
            settings.TWILIO_API_SECRET,
            identity=username
        )
        access_token.add_grant(voice_grant)
        jwt_token = access_token.to_jwt()
        return JsonResponse({"token": jwt_token})