from django.contrib import admin
from models import LinkedInUser

class LinkedInUserAdmin(admin.ModelAdmin):
  fields = ('linked_in_id', 'first_name', 'last_name')

admin.site.register(LinkedInUser, LinkedInUserAdmin)
