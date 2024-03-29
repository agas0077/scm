# Generated by Django 4.2.1 on 2023-05-25 15:53

# Third Party Library
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_alter_event_format_alter_event_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_member_member', to='events.event')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_member_event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='eventmember',
            constraint=models.UniqueConstraint(fields=('member', 'event'), name='unique_member_event'),
        ),
    ]
