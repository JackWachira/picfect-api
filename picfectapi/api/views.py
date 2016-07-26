from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from api.models import Image, Thumbnails
from django.views.decorators.csrf import csrf_exempt
from api.serializers import ImageSerializer, ThumbnailsSerializer
from django.contrib.auth import login
from social.apps.django_app.views import _do_login
from django.core.urlresolvers import reverse

from social.apps.django_app.utils import psa, load_strategy, load_backend


class ImageListView(generics.ListCreateAPIView):
    """Handle GET and POST to /api/images/.
    GET:
        Show all the recent images.
    POST:
        Upload a new image.
    """

    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """GET /api/images/."""
        logged_in_user = self.request.user
        category = self.request.query_params.get('category', None)

        if category:
            return Image.objects.all().filter(uploader=logged_in_user,
                                              category=category)

        return Image.objects.all().filter(uploader=logged_in_user).order_by('date_created')

    def perform_create(self, serializer):
        """POST /api/images/."""
        logged_in_user = self.request.user
        serializer.save(uploader=logged_in_user)


@psa('social:complete')
def auth_by_fb_token(request, backend):
    token = request.GET.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        return user


class Register(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, backend, *args, **kwargs):
        user = auth_by_fb_token(request, backend)
        uri = redirect_uri = "social:complete"
        if uri and not uri.startswith('/'):
            uri = reverse(redirect_uri, args=(backend,))
        if user:
            login(request, user)
            strategy = load_strategy(request)
            backend = load_backend(strategy, backend, uri)
            _do_login(backend, user, user)
            return Response("Login Successful!")
        else:
            return Response("Bad Credentials, check the Token and/or the UID", status=403)


class ThumbnailsView(generics.ListAPIView):

    serializer_class = ThumbnailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        image_id = self.kwargs.get('image_id')
        return Thumbnails.objects.filter(original_image=image_id)
