from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # Let you to search with first name, last name and phone number of the customer
    search_fields = ['email','contact_no']
    list_filter = ['user_role']
    list_display =['email', 'contact_no', 'user_role', 'is_active', 'is_staff']
 #   list_editable = ['contact_no']

admin.site.register(User, UserAdmin)