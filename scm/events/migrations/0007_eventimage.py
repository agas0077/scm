# Generated by Django 4.2.1 on 2023-05-30 12:08

# Third Party Library
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_eventmember_event_alter_eventmember_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='events/gallery/', verbose_name='Изображение')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_image_event', to='events.event', verbose_name='Мероприятие')),
            ],
        ),
    ]
