from django.contrib.auth import get_user_model
from django.db import models

from members.models import MEMBER_NAME

Member = get_user_model()

# Create your models here.

DESCRIPTION_NAME = 'Описание'
APPROVED_NAME = 'Согласовано'
STATUS_NAME = 'Статус пары'
MENTOR_NAME = 'Ментор'
MENTEE_NAME = 'Менти'


class BaseMentorMenteeModel(models.Model):
    description = models.TextField(DESCRIPTION_NAME)
    approved = models.BooleanField(APPROVED_NAME, default=False)

    def __str__(self):
        return self.member.__str__()


class Mentor(BaseMentorMenteeModel):
    member = models.OneToOneField(Member,
                                  verbose_name=MEMBER_NAME,
                                  related_name='mentor',
                                  on_delete=models.CASCADE)


class Mentee(BaseMentorMenteeModel):
    member = models.OneToOneField(Member,
                                  verbose_name=MEMBER_NAME,
                                  related_name='mentee',
                                  on_delete=models.CASCADE)


class MentorMentee(models.Model):
    class Status(models.TextChoices):
        NOT_START = 'not start', 'Еще не начали работу'
        START = 'at work', 'Начали работу'
        STOP = 'end work', 'Закончили работу'

    mentor = models.OneToOneField(Mentor,
                                  verbose_name=MENTOR_NAME,
                                  related_name='mentor_mentee_mentor',
                                  on_delete=models.CASCADE)
    mentee = models.OneToOneField(Mentee,
                                  verbose_name=MENTEE_NAME,
                                  related_name='mentor_mentee_mentee',
                                  on_delete=models.CASCADE)
    
    status = models.CharField(STATUS_NAME,
                              max_length=50,
                              choices=Status.choices,
                              default=Status.NOT_START)

    def __str__(self) -> str:
        mentor = self.mentor.__str__()
        mentee = self.mentee.__str__()
        return f'{mentor} - {mentee}'
