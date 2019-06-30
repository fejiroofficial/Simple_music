from rest_framework import serializers
from .models import Songs


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id', 'title', 'artist')



class TokenSerializer(serializers.Serializer):
    """
    This serializer serializes the data gotten from the token
    """
    token = serializers.CharField(max_length=255)
