from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer, TokenSerializer
from .decorators import validate_post_request


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    """
    POST auth/login/
    """
    # This permission class will overide the global permission
    # class setting
    permission_classes = (permissions.AllowAny,)

    queryset = User.objects.all()

    def login(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            serializer = TokenSerializer(data={
                'token': jwt_encode_handler(
                    jwt_payload_handler(user)
                )
            })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class RegisterUsersView(generics.CreateAPIView):
    """
    POST auth/register/
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        if not username and not password and not email:
            return Response(
                data={
                    "message": "username, password and email is \
                    required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            username=username, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)


class ListCreateSongsView(generics.ListAPIView):
    """
    GET songs/
    POST songs/
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_post_request
    def post(self, request, *args, **kwargs):
        add_a_song = Songs.objects.create(
            title=request.data['title'],
            artist=request.data['artist']
        )
        return Response(
            data=SongsSerializer(add_a_song).data,
            status=status.HTTP_201_CREATED
        )

class SongsOperationsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This is a class useful for getting, updating and deleting
    data
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    def get_a_song(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs['pk'])
            return Response(
                SongsSerializer(a_song).data
            )
        except Songs.DoesNotExist:
            return Response(
                data= 'This song with an id of {} does not exist'.format(kwargs['pk']),  
                status=status.HTTP_404_NOT_FOUND
            )
        
    def put_a_song(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs['pk'])
            serializer = SongsSerializer()
            updated_song = serializer.update(a_song, request.data)
            return Response(SongsSerializer(updated_song).data)
        except Songs.DoesNotExist:
            return Response(
                data={
                    'message': 'This song with an id of {} does not exist'.format(kwargs['pk'])
                },
                status=status.HTTP_404_NOT_FOUND
            )
    
    def delete_a_song(self, request, *args, **kwargs):
        try:
            a_song = self.queryset.get(pk=kwargs['pk'])
            a_song.delete()
            return Response(
                data={
                    'message': 'This song has been deleted successfully'
                },
                status=status.HTTP_204_NO_CONTENT
            )
        except Songs.DoesNotExist:
            return Response(
                data={
                    'message': 'This song with an id of {} does not exist'.format(kwargs['pk'])
                },
                status=status.HTTP_404_NOT_FOUND
            )
