from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.


class CustomUserAdmin(UserAdmin):

    def profile_pic(self, obj):
        return format_html('<img src="{}" width="{}" height="{}" style="border-radius: 50%;"/>'.format(obj.profile_image.url, 30, 30))

    ordering=['id']

    list_display = ('email', 'first_name','profile_pic', 'date_joined', 'last_login','is_active')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login',)

    filter_horizontal = ()
    list_filter = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal Info'), {'fields': ('first_name','last_name')}),
        (
            ('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (('Important dates'), {'fields': ('last_login','date_joined')}),
    )
    readonly_fields = ['last_login', 'date_joined']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


# change Django admin title
admin.site.site_title = 'Blog Admin'

# change Django admin site header
admin.site.site_header = 'Blog Admin'


admin.site.register(User, CustomUserAdmin)
