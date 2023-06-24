from django.contrib import admin
from . models import Profile

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id','username','email')
    search_fields=('id','username','email')
admin.site.register(Profile,ProfileAdmin)
