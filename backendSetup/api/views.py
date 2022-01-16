from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse, Dial
from twilio.jwt.access_token.grants import VideoGrant
from twilio.jwt.access_token import AccessToken, grants
from twilio.rest import Client

client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)


@method_decorator(csrf_exempt, name="dispatch")
class APIView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

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

    def post(self, request, *args, **kwargs):
        room_name = request.POST["roomName"]
        participant_label = request.POST["participantName"]
        response = VoiceResponse()
        
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        room = client.video.rooms.create(unique_name='HELLO')
        print(room)
        return HttpResponse(room)

class TokenView(View):
    @csrf_exempt
    def get(self, request, username, *args, **kwargs):
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

        return JsonResponse({"token": jwt_token})

    @csrf_exempt
    def post(self, request, username, *args, **kwargs):
        print("TEST")

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

        return JsonResponse({"token": jwt_token})

        # return JsonResponse({"token": jwt_token.decode("utf-8")})
