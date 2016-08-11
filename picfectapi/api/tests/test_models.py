import tempfile

from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from PIL import Image
from api import models


def get_temporary_image(temp_file):
    """Generate dummy image file."""
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'jpeg')
    return temp_file


class ImageEditorTest(TestCase):
    """Test accurate creation of models."""

    def setUp(self):
        """Set up new dummy data."""
        user = User.objects.create(
            username='testuser', password='testpassword')
        self.uploader = User.objects.filter(id=user.id).first()

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
        """Check correct image upload and filter creation."""
        to_save = tempfile.NamedTemporaryFile(suffix=".jpg").name
        test_image = get_temporary_image(to_save)
        picture = models.Image.objects.create(
            original_image=test_image, uploader=self.uploader)
        search = models.Image.objects.filter(original_image=test_image).first()
        self.assertEqual(len(models.Image.objects.all()), 1)
        self.assertEqual(len(models.Thumbnails.objects.all()), 11)
        self.assertTrue(models.Thumbnails.objects.get(effect='blur'))
        self.assertIn(test_image, search.original_image.name)
        self.assertIsInstance(picture, models.Image)
