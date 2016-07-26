from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from effects import ImageEffects


CATEGORIES = (
    (1, 'Selfies'), (2, 'Music'),
    (3, 'Fashion'), (4, 'Party'),
    (5, 'Sports'), (6, 'Adventure'),
    (7, 'Miscellanous'), (8, 'School'),
    (9, 'Holiday'), (10, 'Hobby'),
)

filters = ['blur', 'contour', 'detail', 'emboss', 'smooth', 'sharpen']


class Image(models.Model):
    """Model for images."""

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
        return "{}".format(self.original_image)


class Thumbnails(models.Model):
    """Model for thumbnails of edited images"""

    name = models.CharField(max_length=255)
    original_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    effect = models.CharField(max_length=80)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        """Extend parent meta class."""

        ordering = ['-date_modified']


@receiver(post_save, sender=Image)
def create_thumbnails(sender, **kwargs):
    """Generate thumbnails once a photo is uploaded"""
    photo = kwargs.get('instance', '')
    if kwargs.get('created'):
        for filter in filters:
            effect = ImageEffects(photo.original_image, filter)
            thumbnail = Thumbnails()
            thumbnail.name = effect.filters()
            thumbnail.original_image = photo
            thumbnail.effect = filter
            thumbnail.save()
