from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    url(r'^images/$', views.ImageListView.as_view()),
    url(r'^images/edits/(?P<thumbnail_id>[0-9]+)/$',
        views.ImageListView.as_view()),
    url(r'^images/(?P<image_id>[0-9]+)/thumbnails/$',
        views.ThumbnailsView.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$',
        views.ImageDetailView.as_view()),
    url(r'^register/(?P<backend>[^/]+)/', views.Register.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
