from django.contrib import admin

from .models import Contact




admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
	 list_display=("email","date")
# Register your models here.
