from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    url(r'^images/$', views.ImageListView.as_view()),
    url(r'^register/(?P<backend>[^/]+)/', views.Register.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)