from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, verbose_name='Имя пользователя')
    image = models.ImageField(
        upload_to='users_images',
        blank=True,
        null=True,
        verbose_name='Аватар пользователя'
    )

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

        def __str__(self):
            return self.username


