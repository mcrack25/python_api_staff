# Generated by Django 4.1.1 on 2022-09-11 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_alter_department_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ('lname', 'fname', 'sname'), 'verbose_name': 'сотрудник', 'verbose_name_plural': 'сотрудники'},
        ),
    ]
