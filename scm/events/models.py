from django.db import models
from django.contrib.auth import get_user_model

from members.models import MEMBER_NAME

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

EVENT_NAME = 'Мероприятие'

# Create your models here.
Member = get_user_model()


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

    def __str__(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event,
                              verbose_name=EVENT_NAME,
                              on_delete=models.PROTECT,
                              related_name='event_image_event')
    image = models.ImageField(IMAGE_NAME, upload_to='events/gallery/')


class EventMember(models.Model):
    member = models.ForeignKey(Member,
                               verbose_name=MEMBER_NAME,
                               on_delete=models.PROTECT,
                               related_name='event_member_member')
    event = models.ForeignKey(Event,
                              verbose_name=EVENT_NAME,
                              on_delete=models.PROTECT,
                              related_name='event_member_event')

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=['member', 'event'],
                name='unique_member_event'
            ),
        )
