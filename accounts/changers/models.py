from django.db import models
from django.utils.translation import gettext_lazy as _
from core.base.models import AddressMixin, PhoneMixin
from core.base.enums.natural import SexPersonChoice

class Changer(AddressMixin, PhoneMixin):
    user = models.OneToOneField("users.User", verbose_name=_("Usuário"), on_delete=models.PROTECT)
    bench = models.ForeignKey("benches.Bench", verbose_name=_("Banca"), on_delete=models.SET_NULL, null=True, blank=True)    
    name = models.CharField(_("Nome"), max_length=80)
    cpf = models.CharField(_("CPF"), max_length=20, unique=True)
    sex = models.CharField(_("Sexo"), max_length=15, choices=SexPersonChoice.choices)
    is_active = models.BooleanField(_("Está ativo?"), default=True)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)

    class Meta:
        verbose_name = 'Cambista'
        verbose_name_plural = 'Cambistas'

    def __str__(self):
        return self.name