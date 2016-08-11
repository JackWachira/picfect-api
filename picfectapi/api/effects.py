import os

from django.conf import settings
from PIL import Image, ImageFilter, ImageOps


class ImageEffects(object):
    """Handle image effects and filters."""

    def __init__(self, image, effect):
        """Initialize image effects class."""

        self.image = Image.open(image)
        if (self.image.mode == 'RGBA'):
            self.image.load()
            r, g, b, a = self.image.split()
            self.image = Image.merge('RGB', (r, g, b))

        self.effect = effect
        self.image_name = image.name
        path = settings.MEDIA_ROOT + '/temp/'
        if not os.path.exists(path):
            os.makedirs(path)
        self.file_path = path + \
            effect + os.path.basename(self.image_name)

    def filters(self):
        """Handle Filters on images."""

        if self.effect == 'blur':
            edited_image = self.image.filter(ImageFilter.BLUR)
        if self.effect == 'contour':
            edited_image = self.image.filter(ImageFilter.CONTOUR)
        if self.effect == 'emboss':
            edited_image = self.image.filter(ImageFilter.EMBOSS)
        if self.effect == 'detail':
            edited_image = self.image.filter(ImageFilter.DETAIL)
        if self.effect == 'smooth':
            edited_image = self.image.filter(ImageFilter.SMOOTH)
        if self.effect == 'sharpen':
            edited_image = self.image.filter(ImageFilter.SHARPEN)
        edited_image.save(self.file_path)

        if "picfectapi/" in self.file_path:
            return self.file_path.split("picfectapi/", 1)[1]
        return self.file_path

    def operations(self):
        """Handle other simple image operations."""
        if self.effect == 'flip':
            edited_image = ImageOps.flip(self.image)
        if self.effect == 'mirror':
            edited_image = ImageOps.mirror(self.image)
        if self.effect == 'solarize':
            edited_image = ImageOps.solarize(self.image)
        if self.effect == 'posterize':
            edited_image = ImageOps.posterize(self.image, 1)
        if self.effect == 'grayscale':
            edited_image = ImageOps.grayscale(self.image)
        edited_image.save(self.file_path)

        if "picfectapi/" in self.file_path:
            return self.file_path.split("picfectapi/", 1)[1]
        return self.file_path
