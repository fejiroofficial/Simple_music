from rest_framework.response import Response
from rest_framework.views import status

def validate_post_request(func):
    def decorated(*args, **kwargs):
        title = args[0].request.data.get('title', '')
        artist = args[0].request.data.get('artist', '')

        if not title or not artist:
            return Response(
                data={
                    'message': 'You cannot add a new song without an artist and a song'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return func(*args, **kwargs)
    return decorated
