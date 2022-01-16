from django.shortcuts import render
from twilio.rest import Client

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from twilio.twiml.voice_response import VoiceResponse, Dial
from django.conf import settings
from twilio.jwt.access_token import AccessToken, grants
from django.views.decorators.csrf import csrf_exempt

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

@method_decorator(csrf_exempt, name="dispatch")
class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html", {})

class RoomView(View):
    def get(self, request, *args, **kwargs):
        rooms = client.conferences.stream(
            status="in-progress"
        )
        rooms_reps = [
            {
                "room_name": conference.friendly_name,
                "sid": conference.sid,
                "participants": [
                        p.label for p in conference.participants.list()
                    ],
                "status": conference.status,
            } for conference in rooms]
        return JsonResponse({"rooms": rooms_reps})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        room_name = request.POST["roomName"]
        participant_label = request.POST["participantLabel"]
        response = VoiceResponse()
        dial = Dial()
        dial.conference(
            name=room_name,
            participant_label=participant_label,
            start_conference_on_enter=True,
        )
        response.append(dial)
        return HttpResponse(response.to_xml(), content_type="text/xml")

class TokenView(View):
    @csrf_exempt
    def post(self, request, username, *args, **kwargs):
        voice_grant = grants.VoiceGrant(
            outgoing_application_sid=settings.TWIML_APPLICATION_SID,
            incoming_allow=True,
        )
        
        video_grant = grants.VideoGrant(room='My Room')


        access_token = AccessToken(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_API_KEY,
            settings.TWILIO_API_SECRET,
            identity=username
        )

        # access_token.add_grant(voice_grant)
        access_token.add_grant(video_grant)

        jwt_token = access_token.to_jwt()
        return JsonResponse({"token": jwt_token.decode("utf-8")})

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
        return JsonResponse({"token": jwt_token.decode("utf-8")})