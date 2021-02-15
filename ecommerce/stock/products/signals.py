from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save, pre_delete
from ecommerce.stock.products.models import ImageProduct

@receiver(pre_save, sender=ImageProduct)
def save_image_product(sender, instance:ImageProduct, *args, **kwargs):
  # set is_main_image for another images
  if instance.is_main_image:
    ImageProduct.objects.filter(
      product=instance.product
    ).exclude(pk=instance.pk).update(is_main_image=False)


@receiver(pre_delete, sender=ImageProduct)
def delete_image_product(sender, instance:ImageProduct, *args, **kwargs):
  # call delete if no has another images by product
  qs = ImageProduct.objects.filter(
      product=instance.product
    ).exclude(pk=instance.pk)
  if not qs.exists():
    raise Exception(_('Your product must have an image!'))

  if instance.is_main_image:
    first_image = qs.first()
    qs.filter(pk=first_image.pk).update(is_main_image=True)