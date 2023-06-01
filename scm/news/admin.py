from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in News._meta.get_fields()]


admin.site.register(News, NewsAdmin)
