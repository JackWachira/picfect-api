import os
from PIL import Image, ImageFilter, ImageOps
from django.conf import settings


class ImageEffects(object):
    """Handle image effects and filters."""

    def __init__(self, image, effect, temp=False):
        """Initialize image effects class."""
        self.image = Image.open(image)
        self.effect = effect
        self.image_name = image.name
        path = settings.MEDIA_ROOT + '/edited/'
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
        return self.file_path

    def operations(self):
        """Handle other simple image operations."""
        if self.effect == 'flip':
            edited_image = ImageOps.flip(self.image)
        if self.effect == 'mirror':
            edited_image = ImageOps.mirror(self.image)
        if self.effect == 'invert':
            edited_image = ImageOps.invert(self.image)
        if self.effect == 'grayscale':
            edited_image = ImageOps.grayscale(self.image)
        edited_image.save(self.file_path)
        return self.file_path
