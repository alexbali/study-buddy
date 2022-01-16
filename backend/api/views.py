from django.shortcuts import render
from twilio.rest import Client

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.conf import settings
from twilio.jwt.access_token import AccessToken, grants
from django.views.decorators.csrf import csrf_exempt
import json

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

# @method_decorator(csrf_exempt, name="dispatch")
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
        room = client.video.rooms.create(
            unique_name=room_name,
            type="group",
            max_participants=max_participants,
        )
        
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