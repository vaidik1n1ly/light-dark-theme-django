from django.apps import AppConfig
from django.db.models.signals import post_migrate

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from .signals import create_default_user_and_setting

        post_migrate.connect(create_default_user_and_setting, sender=self)