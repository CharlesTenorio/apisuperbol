from django.db import models
from django.utils.translation import gettext_lazy as _
# from core.base.models import AddressMixin, PhoneMixin
from core.base.fields import CpfCnpjField
from core.base.enums.natural import CompanyTypeChoices


class Store(models.Model):
    owner = models.ForeignKey("owners.Owner", verbose_name=_("Proprietário"),
                              on_delete=models.CASCADE)
    company_name = models.CharField(_("Razão social"), max_length=250)
    fantasy_name = models.CharField(
        _("Nome Fantasia"), max_length=250, blank=True, null=True)
    cpf_cnpj = CpfCnpjField()
    type = models.SmallIntegerField(
        _("TIpo de empresa"), choices=CompanyTypeChoices.choices, default=CompanyTypeChoices.INDIVIDUAL)
    created_at = models.DateTimeField(_("Criado em"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Atualizado em"), auto_now=True)
