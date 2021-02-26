from django.db import models
from django.utils.translation import gettext_lazy as _

from core.base.models import AddressMixin, PersonDocumentMixin, PhoneMixin
from accounts.users.models import User


class Owner(PersonDocumentMixin, PhoneMixin, AddressMixin):
  user = models.ForeignKey("users.User", verbose_name=_("Usuário"), on_delete=models.CASCADE)
  name = models.CharField(_("Nome"), max_length=200)

  def __str__(self) -> str:
    return self.name

  class Meta:
    verbose_name = 'Proprietario'
    verbose_name_plural = 'Proprietários'