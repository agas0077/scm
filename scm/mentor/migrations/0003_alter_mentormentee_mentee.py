# Generated by Django 4.2.1 on 2023-05-29 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_alter_mentee_member_alter_mentor_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentormentee',
            name='mentee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_mentee_mentee', to='mentor.mentee', verbose_name='Менти'),
        ),
    ]
