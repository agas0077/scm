# Generated by Django 4.2.1 on 2023-05-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0004_alter_mentormentee_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='basementormenteemodel',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Согласовано'),
        ),
    ]