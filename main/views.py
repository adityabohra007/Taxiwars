from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer, CreatedGameSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY


class GameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        instance = Game.objects.filter(created_by=request.user)
        serializer = CreatedGameSerializer(instance, many=True)
        return Response(serializer.data)


class GetGameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        data = Game.objects.filter(
            id=pk, created_by=self.request.user)
        return Response(data.get().string)


class StartGameView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        new_game = Game(string="")
        new_game.save()
        serializer = CreatedGameSerializer(new_game)
        return Response(serializer.data['id'])


class UpdateBoard(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        print(request.POST)
        game_id = request.POST['game_id']
        word = request.POST['word']
        update_game = Game.objects.filter(id=game_id)
        temp = 0
        game_string = update_game.get().string
        if len(game_string) >= 6:
            while temp < (len(game_string)//2):
                if game_string[temp] == game_string[len(game_string)-temp-1]:
                    temp += 1
                else:
                    return Response({'palindrome': False})
            return Response({'palindrome': True, 'string': game_string})

        if len(word) != 1 or not word.isalpha():
            return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)
        import random
        digit = random.randint(0, 9)

        if update_game.exists():
            update_game = update_game.first()
            update_game.string = update_game.string+word+str(digit)
            update_game.save()
        serializer = GameSerializer(update_game)
        return Response(serializer.data)
