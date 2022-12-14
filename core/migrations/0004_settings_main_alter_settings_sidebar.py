# Generated by Django 4.1.1 on 2022-09-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0004_alter_staff_options'),
        ('core', '0003_settings_delete_sidebar'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='main',
            field=models.ManyToManyField(blank=True, related_name='main', to='staff.department', verbose_name='Руководство (подразделения)'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='sidebar',
            field=models.ManyToManyField(blank=True, related_name='sidebar', to='staff.department', verbose_name='Сайдбар (подразделения)'),
        ),
    ]
