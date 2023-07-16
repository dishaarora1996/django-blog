from django.contrib import admin
from .models import User
# Register your models here.


# change Django admin title
admin.site.site_title = 'Blog Admin'

# change Django admin site header
admin.site.site_header = 'Blog Admin'


admin.site.register(User)
