# Generated by Django 4.2.1 on 2023-06-08 10:49

# Third Party Library
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.ImageField(blank=True, help_text='Соотношение сторон: 1:1', null=True, upload_to='company_logo/', verbose_name='Лого компании')),
                ('company', models.CharField(max_length=200, verbose_name='Компания')),
            ],
        ),
    ]
