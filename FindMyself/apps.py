from django.apps import AppConfig


class FindmyselfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FindMyself'
    def ready(self):
        import FindMyself.signals