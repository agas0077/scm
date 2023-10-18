# Third Party Library
from community.models import CompanyLogo
from django.contrib import admin

# Register your models here.


class CompanyLogoAdmin(admin.ModelAdmin):
    fields = (
        "company",
        "company_logo",
    )
    list_filter = (("company_logo", admin.EmptyFieldListFilter),)
    list_display = ("company",)


admin.site.register(CompanyLogo, CompanyLogoAdmin)
