from django.apps import AppConfig


class ElasticsearchappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'elasticsearchapp'

    def ready(self):
        import elasticsearchapp.signals
