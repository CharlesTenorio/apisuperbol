from decouple import config
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration


if SENTRY_DSN := config("SENTRY_DSN", default=None):
  sentry_sdk.init(
      dsn=SENTRY_DSN,
      integrations=[DjangoIntegration(), CeleryIntegration(), RedisIntegration()],
      traces_sample_rate=0.0,
  )