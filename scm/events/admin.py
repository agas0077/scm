# Third Party Library
from django.contrib import admin
from events.models import Event, EventImage, EventMember


class BaseAdmin(admin.ModelAdmin):
    pass


class EventImageAdmin(BaseAdmin):
    list_display = [field.name for field in EventImage._meta.get_fields()]


admin.site.register(Event, BaseAdmin)
admin.site.register(EventMember, BaseAdmin)
admin.site.register(EventImage, EventImageAdmin)
