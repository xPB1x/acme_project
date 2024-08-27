from django.apps import AppConfig


class BirthdayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'birthday'
    verbose_name = 'День рождения'
    verbose_name_plural = 'Дни рождения'
