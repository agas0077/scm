from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

NAME_NAME = 'Имя'
SURNAME_NAME = 'Фамилия'
EMAIL_NAME = 'Почта'
PHONE_NUM_NAME = 'Номер телефона'
CITY_NAME = 'Город'
TELEGRAM_NAME = 'Ник в Telegram'
BD_NAME = 'Дата рождения'
COMPANY_NAME = 'Компания'
JOB_NAME = 'Должность'
TERMS_AGREE_NAME = 'Согласие на обработку персональных данных'
APPROVED_NAME = 'Одобрен'

IMAGE_NAME = 'Изображение'
IS_STAFF_NAME = 'Сотрудник'
IS_SUPERUSER_NAME = 'Суперюзер'
IS_ACTIVE_NAME = 'Активный пользователь'
STAFF_JOB_NAME = 'Должность в проекте'
EDUCATION_NAME = 'Образование'

PHONE_NUM_ERROR = 'Формат должен быть: +99999999999'

# Create your models here.

DATE_FIELDS = ['birthday']
MEMBER_NAME = 'Участник'


class CustomUserManager(BaseUserManager):
    """
    Кастомный менеджер user model, который использует поле email в качестве
    уникального идентификатора, вместо username.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Создает и сохранеяет объект пользователя с email и password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Создает и сохранеяет объект супер-пользователя с email и password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class Member(AbstractBaseUser, PermissionsMixin):
    """Модель пользователя"""

    phone_number_regex = RegexValidator(regex=r'^\+?\d{8,15}$',
                                        message=PHONE_NUM_ERROR)

    REQUIRED_FIELDS = ['name', 'surname', 'phone_num',
                       'city', 'telegram', 'birthday', 'company',
                       'job', 'terms_agree', 'approved']

    USERNAME_FIELD = 'email'
    username = None
    objects = CustomUserManager()

    email = models.EmailField(EMAIL_NAME, 
                              max_length=254,
                              unique=True, 
                              error_messages={
                                  'unique': ('Пользователь с такой '
                                             'почтой уже зарегистрирован')
                              })

    name = models.CharField(NAME_NAME, max_length=200)
    surname = models.CharField(SURNAME_NAME, max_length=200)
    phone_num = models.CharField(PHONE_NUM_NAME,
                                 validators=[phone_number_regex, ],
                                 max_length=16,
                                 unique=True,
                                 error_messages={
                                     'unique': ('Пользователь с таким номером '
                                                'уже зарегистрирован')
                                 })
    city = models.CharField(CITY_NAME, max_length=200)
    telegram = models.CharField(TELEGRAM_NAME,
                                max_length=200,
                                unique=True)
    birthday = models.DateField(BD_NAME)
    company = models.CharField(COMPANY_NAME, max_length=200)
    job = models.CharField(JOB_NAME, max_length=200)
    terms_agree = models.BooleanField(TERMS_AGREE_NAME, default=False)
    approved = models.BooleanField(APPROVED_NAME, default=False)

    image = models.ImageField(
        IMAGE_NAME, upload_to='members/', blank=True, null=True)
    staff_job = models.CharField(
        STAFF_JOB_NAME, max_length=200, blank=True, null=True)
    education = models.CharField(
        EDUCATION_NAME, max_length=200, blank=True, null=True)

    is_staff = models.BooleanField(
        IS_STAFF_NAME,
        default=False,
        help_text='Определяет есть ли у пользователя досутп к адиминке.',
    )
    is_superuser = models.BooleanField(
        IS_SUPERUSER_NAME,
        default=False,
    )
    is_active = models.BooleanField(
        IS_ACTIVE_NAME,
        default=True,
    )

    def __str__(self):
        return f'{self.name} {self.surname}'
