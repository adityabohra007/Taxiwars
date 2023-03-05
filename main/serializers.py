from rest_framework.serializers import ModelSerializer
from .models import Game


class CreatedGameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['id']


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = ['string']
