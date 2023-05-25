# Generated by Django 4.2.1 on 2023-05-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='news/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=200, verbose_name='Категория')),
                ('description', models.CharField(max_length=200, verbose_name='Краткое описание')),
                ('text', models.TextField(verbose_name='Краткое описание')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]