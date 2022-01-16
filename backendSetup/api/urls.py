from django.urls import path

from api.views import RoomView, TokenView,APIView

urlpatterns = [
    path("api", APIView.as_view(), name="api_home"),
    path("rooms", RoomView.as_view(), name="room_list"),
    path("token/<username>", TokenView.as_view(), name="token"),
]
