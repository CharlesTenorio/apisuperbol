from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.files.images import get_image_dimensions


def validade_dimensions_image_product(image):
  width, height = get_image_dimensions(image)
  if width < 300:
    raise ValidationError(
      _('%(width)s is very small width'),
      params={'width': width},
    )
  if height < 300:
    raise ValidationError(
      _('%(height)s is very small width'),
      params={'height': height},
    )