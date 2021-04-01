from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.fields import CpfField

def customer_path(instance, filename):
  return f"{instance.user.username}/profile/{filename}"

class Customer(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.PROTECT)
    name = models.CharField(_("Nome"), max_length=40)
    prolile = models.ImageField(
      verbose_name=_("Foto de perfil"),
      upload_to=customer_path,
      max_length=255,
      null=True,  blank=True
      )
    birth_date = models.DateField()
    cpf = CpfField(verbose_name=_("CPF"), unique=True)
    pix_key = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'