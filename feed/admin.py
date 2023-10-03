from django.contrib import admin
from . models import Feed

class FeedAdmin(admin.ModelAdmin):
    readonly_fields=("id","related_id")

admin.site.register(Feed,FeedAdmin)
