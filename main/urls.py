
from django.urls import path
from .views import GameView, StartGameView, UpdateBoard, GetGameView
urlpatterns = [
    path("game/", GameView.as_view(), name='Game'),
    path("game/start", StartGameView.as_view(), name='Game'),
    path("game/update", UpdateBoard.as_view(), name=""),
    path("game/<int:pk>", GetGameView.as_view(), name="")

]
