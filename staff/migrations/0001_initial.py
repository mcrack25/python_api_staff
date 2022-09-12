# Generated by Django 4.1.1 on 2022-09-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, verbose_name='Название подразделения')),
                ('numbers', models.JSONField(blank=True, null=True, verbose_name='Номера')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.department', verbose_name='Родительское подразделение')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название должности')),
                ('priority', models.PositiveIntegerField(default=1000, verbose_name='Приоритет')),
            ],
        ),
        migrations.CreateModel(
            name='PostType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тип должности')),
                ('priority', models.PositiveIntegerField(default=1000, verbose_name='Приоритет')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('fname', models.CharField(max_length=50, verbose_name='Имя')),
                ('sname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='Номер')),
                ('photo', models.ImageField(blank=True, upload_to='staff/images', verbose_name='Фото')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.department', verbose_name='Подразделение')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.post', verbose_name='Должность')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.posttype', verbose_name='Тип должности'),
        ),
    ]
