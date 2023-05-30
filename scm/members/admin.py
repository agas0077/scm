from django.contrib import admin
from members.models import Member
from django.contrib.auth.admin import UserAdmin


class MemberAdmin(UserAdmin):
    fieldsets = (
        ('Личная информация', {
         'fields': ('password', 'name', 'surname', 'city', 'birthday')}),
        ('Контакты', {'fields': ('email', 'phone_num', 'telegram',)}),
        ('Работа', {'fields': ('company', 'job',)}),
        ('Сотрудники', {
         'fields': ('is_staff', 'is_superuser', 'staff_job', 'education',
                    'image', 'groups')}),
        ('Согласование', {
         'fields': ('terms_agree', 'approved', 'is_active')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ['email', 'password1', 'password2',] + Member.REQUIRED_FIELDS,
            },
        ),
    )
    exclude = ('username', 'date_joined')
    list_display = ('email', 'name', 'surname', 'is_staff')
    search_fields = ('name', 'surname', 'email')
    list_filter = ('approved',)
    ordering = None
    list_display = ('email', 'name', 'surname')
    empty_value_display = '-пусто-'


admin.site.register(Member, MemberAdmin)
