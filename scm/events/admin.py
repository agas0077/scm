from django.contrib import admin
from events.models import Event

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event()._meta.get_fields()]
    pass

admin.site.register(Event, MemberAdmin)