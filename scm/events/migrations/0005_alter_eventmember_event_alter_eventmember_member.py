# Generated by Django 4.2.1 on 2023-05-26 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_eventmember_eventmember_unique_member_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventmember',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_member_event', to='events.event'),
        ),
        migrations.AlterField(
            model_name='eventmember',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_member_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
