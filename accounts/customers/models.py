from django.db import models
from django.utils.translation import gettext_lazy as _

# from core.base.models import AddressMixin, PersonDocumentMixin, PhoneMixin
from .mixins import CustomerMixin


class Customer(CustomerMixin):
  user = models.ForeignKey("users.User", verbose_name=_("Usuário"), on_delete=models.CASCADE)

  def __str__(self):
    return self.name