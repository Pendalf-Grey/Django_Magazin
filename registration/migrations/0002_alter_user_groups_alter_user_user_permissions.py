# Generated by Django 4.2.7 on 2024-01-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='Группы, к которым принадлежит данный пользователь. Пользователь получит все права, указанные в каждой из его/её групп.', related_name='custom_users_groups', related_query_name='custom_user_group', to='auth.group', verbose_name='группы'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Индивидуальные права данного пользователя.', related_name='custom_users_permissions', related_query_name='custom_user_permission', to='auth.permission', verbose_name='user_permissions'),
        ),
    ]
