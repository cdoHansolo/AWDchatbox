from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_of_birth','gender') #display fields
    list_filter = ('gender') #filtering gender
    search_fields = ('user__username', 'date_of_birth', 'gender__gender') #search the contents
 
admin.site.register(UserProfile, UserProfileAdmin)