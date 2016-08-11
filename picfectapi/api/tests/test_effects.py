import tempfile

from django.contrib.auth.models import User
from django.test import override_settings
from django.test import TestCase
from PIL import Image

from api import models
from api.effects import ImageEffects


def get_temporary_image(temp_file):
    """Generate dummy image file."""
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'jpeg')
    return temp_file


class TestEffects(TestCase):

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUp(self):
        """Set up new dummy user data."""

        user = User.objects.create(
            username='testuser', password='testpassword')
        self.uploader = User.objects.filter(id=user.id).first()

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def filter(self, effect_type, operation):
        test_user = User.objects.get(id=1)
        temp_file = tempfile.NamedTemporaryFile(suffix=".jpg")
        test_image = get_temporary_image(temp_file)
        picture = models.Image.objects.create(
            original_image=test_image.name, uploader=test_user)
        effect = ImageEffects(picture.original_image, effect_type)
        if operation == 'filters':
            response = effect.filters()
        else:
            response = effect.operations()
        self.assertIn(effect_type, response)

    def test_applying_filters(self):
        """Test whether filters are applied."""

        for key, value in models.effects_list.iteritems():
            for effect_type in value:
                self.filter(effect_type, key)
