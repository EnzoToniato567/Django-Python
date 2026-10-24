from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'src'
    label = 'core'

    def ready(self):
        from . import register
