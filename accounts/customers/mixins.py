from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomerMixin(models.Model):
  user = models.ForeignKey("users.User", verbose_name=_("Usuário"), on_delete=models.CASCADE)
  name = models.CharField(_("Nome"), max_length=200)
  nick_name = models.CharField(_("Nick"), max_length=200, null=True, blank=True)
  shopping_cart = models.ManyToManyField(
    'products.Product',
    related_name='shoping_cart',
    verbose_name=_('Carrinho de compras'),
    blank=True
  )
  wishlist = models.ManyToManyField(
    'products.Product',
    related_name='wishlist',
    verbose_name=_('Lista de desejos'),
    blank=True
  )

  class Meta:
    abstract = True
    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'