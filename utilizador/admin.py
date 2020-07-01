from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import utilizador
from django.contrib.auth.admin import UserAdmin

class Admin(UserAdmin):
	list_display = ('email','username','Nome','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(utilizador, Admin)

