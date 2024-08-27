from django.db import models

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        'Фамилия',
        blank=True, 
        help_text='Необязательное поле',
        max_length=20
    )
    birthday = models.DateField('Дата Рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        verbose_name = 'ДР Пользователя'
        verbose_name_plural = 'ДР Пользователей'
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
