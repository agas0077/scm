from django.db import models

LOGO_NAME = 'Лого компании'
COMPANY_NAME = 'Компания'

# Create your models here.


class CompanyLogo(models.Model):
    company_logo = models.ImageField(LOGO_NAME,
                                     upload_to='company_logo/',
                                     blank=True,
                                     null=True,
                                     help_text='Соотношение сторон: 1:1')
    company = models.CharField(COMPANY_NAME, max_length=200)
