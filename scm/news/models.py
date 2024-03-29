# Third Party Library
from django.db import models

TITLE_NAME = "Заголовок"
IMAGE_NAME = "Изображение"
CATEGORY_NAME = "Категория"
DESCRIPTION_NAME = "Краткое описание"
TEXT_NAME = "Текст"
DATE_NAME = "Дата"


class News(models.Model):
    title = models.CharField(TITLE_NAME, max_length=100)
    image = models.ImageField(
        IMAGE_NAME, upload_to="news/", help_text="Соотношение сторон: 1.33:1"
    )
    category = models.CharField(CATEGORY_NAME, max_length=200)
    description = models.CharField(DESCRIPTION_NAME, max_length=200)
    text = models.TextField(TEXT_NAME)
    date = models.DateField(DATE_NAME, auto_now_add=True)
