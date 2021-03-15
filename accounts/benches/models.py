from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.models import AddressMixin, PhoneMixin, PersonDocumentMixin

class Bench(PersonDocumentMixin, PhoneMixin, AddressMixin):
    user = models.OneToOneField("users.User", verbose_name=_("Usuário"), on_delete=models.PROTECT)
    name = models.CharField(_("Nome da banca"), max_length=250, unique=True)
    responsible = models.CharField(_("Nome do responsável"), max_length=250)
    is_active = models.BooleanField(_("Está ativo?"), default=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
    
    def __str__(self):
        return self.nome_banca

    class Meta:
        managed = True
        verbose_name = 'Banca'
        verbose_name_plural = 'Bancas'