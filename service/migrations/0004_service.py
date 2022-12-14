# Generated by Django 4.1.4 on 2022-12-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_alter_client_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Услуга')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(blank=True, max_length=100, verbose_name='Цена')),
                ('duration', models.PositiveIntegerField(blank=True, max_length=100, verbose_name='Длительность (часов)')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
        ),
    ]
