from django.apps import AppConfig
from django.db.models import base


class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals