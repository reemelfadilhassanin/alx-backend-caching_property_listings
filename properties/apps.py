from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    name = 'properties'
from django.apps import AppConfig


class PropertiesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'properties'

    def ready(self):
        import properties.signals
