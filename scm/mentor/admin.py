# Third Party Library
from django.contrib import admin
from mentor.models import Mentee, Mentor, MentorMentee


class BaseAdmin(admin.ModelAdmin):
    list_filter = ("approved",)


class MenorMenteeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mentor, BaseAdmin)
admin.site.register(Mentee, BaseAdmin)
admin.site.register(MentorMentee, MenorMenteeAdmin)
