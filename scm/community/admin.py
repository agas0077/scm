from django.contrib import admin

from community.models import CompanyLogo

# Register your models here.


class CompanyLogoAdmin(admin.ModelAdmin):
    fields = ('company', 'company_logo',)
    list_filter = (
        ('company_logo', admin.EmptyFieldListFilter),
    )
    list_display = ('company', )


admin.site.register(CompanyLogo, CompanyLogoAdmin)
