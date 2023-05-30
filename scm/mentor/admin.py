from django.contrib import admin

from mentor.models import Mentor, Mentee, MentorMentee

# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mentor, BaseAdmin)
admin.site.register(Mentee, BaseAdmin)
admin.site.register(MentorMentee, BaseAdmin)