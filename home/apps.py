from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        from . import signals
        from .cron import refresh_news_cache
        # Run immediately when server starts
        refresh_news_cache()

