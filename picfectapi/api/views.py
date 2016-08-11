from django.contrib.auth import login
from django.core.files import File
from django.core.urlresolvers import reverse
from rest_framework import generics, permissions
from rest_framework.decorators import permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from social.apps.django_app.utils import load_backend, load_strategy, psa
from social.apps.django_app.views import _do_login

from api.models import Image, Thumbnails
from api.serializers import ImageSerializer, ThumbnailsSerializer


class ImageListView(generics.ListCreateAPIView):
    """Handle GET and POST to /api/images/.
    GET:
        Shows all the images.
    POST:
        Upload a new image.
    """

    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """GET /api/images/."""

        logged_in_user = self.request.user
        return Image.objects.all().filter(uploader=logged_in_user).order_by('date_created')

    def perform_create(self, serializer):
        """POST /api/images/."""

        logged_in_user = self.request.user
        edited_image = self.kwargs.get('thumbnail_id')
        if edited_image:
            thumb = Thumbnails.objects.get(pk=edited_image)
            with open(thumb.name, 'rb') as doc_file:
                serializer.save(uploader=logged_in_user,
                                original_image=File(doc_file))
        else:
            serializer.save(uploader=logged_in_user)


class ImageDetailView(generics.RetrieveUpdateAPIView):
    """Handle PUT to /api/images/.
    PUT:
        Returns updated image
    """

    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        category = self.request.data.get('category', None)
        serializer.save(category=category)


@psa('social:complete')
def auth_by_fb_token(request, backend):
    token = request.GET.get('access_token')
    user = request.backend.do_auth(token)
    if user:
        return user


class Register(APIView):
    """Handle GET to /api/register/(?P<backend>[^/]+)/
    GET:
        Returns login status
    """
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
    """Handle GET to api/images/(?P<image_id>[0-9]+)/thumbnails/
    GET:
        Returns edited thumbnails of an image
    """
    serializer_class = ThumbnailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        image_id = self.kwargs.get('image_id')
        return Thumbnails.objects.filter(original_image=image_id)
