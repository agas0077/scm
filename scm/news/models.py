from django.db import models

TITLE_NAME = 'Заголовок'
IMAGE_NAME = 'Изображение'
CATEGORY_NAME = 'Категория'
DESCRIPTION_NAME = 'Краткое описание'
TEXT_NAME = 'Текст'
DATE_NAME = 'Дата'

# Create your models here.


class News(models.Model):
    title = models.CharField(TITLE_NAME, max_length=100)
    image = models.ImageField(IMAGE_NAME, upload_to='news/')
    category = models.CharField(CATEGORY_NAME, max_length=200)
    description = models.CharField(DESCRIPTION_NAME, max_length=200)
    text = models.TextField(DESCRIPTION_NAME)
    date = models.DateField(DATE_NAME, auto_now_add=True)
