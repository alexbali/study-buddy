from django.urls import path

from api.views import RoomView, TokenView, TestView

urlpatterns = [
    path("rooms", RoomView.as_view(), name="room_list"),
    path("token/<username>", TokenView.as_view(), name="token"),
    path("test", TestView.as_view(), name="test"),
]
