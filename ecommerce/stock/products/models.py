from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.enums.products import UnitOfMeasurementChoice
from ecommerce.stock.products.utils import product_image_path
from ecommerce.stock.products.validators import validade_dimensions_image_product

class Product(models.Model):
  name = models.CharField(_("Nome"), max_length=80)
  brand = models.ForeignKey(
    "brands.Brand",
    verbose_name=_("Marca"),
    on_delete=models.CASCADE
  )
  description = models.CharField(_("Descrição"), max_length=50)
  wholesale_price = models.DecimalField(_("Preço de atacado"), max_digits=5, decimal_places=2)
  retail_price = models.DecimalField(_("Preço de revenda"), max_digits=5, decimal_places=2)
  product_code = models.CharField(_("Código do produto"), max_length=150)
  quantity_products = models.PositiveIntegerField(_("Quantidade de produtos"), default=1)
  unit_measurement_type = models.CharField(
    _("Tipo de unidade de medida"), max_length=50,
    choices=UnitOfMeasurementChoice.choices,
    default=UnitOfMeasurementChoice.G
  )
  unit_measurement_value = models.FloatField(_("Valor da unidade de medida"))
  store = models.ForeignKey(
    "stores.Store",
    verbose_name=_("Loja"),
    on_delete=models.CASCADE
  )
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

  @property
  def profit(self):
    return self.wholesale_price - self.retail_price

  def __str__(self):
    return f'{self.name} ({self.retail_price})'

  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'



class ImageProduct(models.Model):
  product = models.ForeignKey(Product,
    verbose_name=_("Produto"),
    on_delete=models.CASCADE
  )
  img = models.ImageField(
    upload_to=product_image_path,
    validators=[validade_dimensions_image_product],
    max_length=255,
    verbose_name='Foto',
    blank=True, null=True
  )
  is_main_image = models.BooleanField(_("Imagem principal?"), default=False)
  created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

class Meta:
    verbose_name = 'Imagem de produto'
    verbose_name_plural = 'Imanges de produtos'