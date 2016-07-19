from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models


CATEGORIES = (
    (1, 'Selfies'), (2, 'Music'),
    (3, 'Fashion'), (4, 'Party'),
    (5, 'Sports'), (6, 'Adventure'),
    (7, 'Miscellanous'), (8, 'School'),
    (9, 'Holiday'), (10, 'Hobby'),
)


class Image(models.Model):
    """Model for storing images."""

    name = models.CharField(max_length=255, blank=True)
    original_image = models.ImageField(upload_to='images/', blank=False)
    edited_image = models.ImageField(upload_to='edited/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)
    category = models.IntegerField(choices=CATEGORIES, default=9)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)

    def __unicode__(self):
        """String representation of an image.
        Returns:
            The name of the image
        """
        return "{}".format(self.name)
