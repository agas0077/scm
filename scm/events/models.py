from django.db import models

TITLE_NAME = 'Заголовок'
SHORT_DESCRIPTION_NAME = 'Краткое описание'
DATE_NAME = 'Дата'
START_TIME_NAME = 'Время начала'
END_TIME_NAME = 'Время окончания'
IMAGE_NAME = 'Изображение'
SPEAKER_NAME = 'Спикер'
FORMAT_NAME = 'Формат'
TEXT_NAME = 'Текст'
DESCRIPTION_NAME = 'Описание'

# Create your models here.


class Event(models.Model):

    class Format(models.TextChoices):
        ONLINE = 'ONLINE', 'Онлайн'
        OFFLINE = 'OFFLINE', 'Оффлайн'
        HYBRID = 'HYBRID', 'Гибрид'

    title = models.CharField(TITLE_NAME, max_length=100)
    description = models.CharField(SHORT_DESCRIPTION_NAME, max_length=200)
    date = models.DateField(DATE_NAME)
    start_time = models.TimeField(START_TIME_NAME)
    end_time = models.TimeField(END_TIME_NAME)
    image = models.ImageField(IMAGE_NAME, upload_to='events/')
    speaker = models.CharField(SPEAKER_NAME, max_length=100)
    format = models.CharField(FORMAT_NAME,
                              choices=Format.choices,
                              default=Format.OFFLINE,
                              max_length=7)
    text = models.TextField(DESCRIPTION_NAME)
