from django.contrib import admin
from .models import Event,Status,EventEditorChoice


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('id','created','poster','host_phone_number','is_deleted')
    search_fields = (
        'id',
        'title',
        'host'
    )

class EditorChoiceAdmin(admin.ModelAdmin):
        readonly_fields=('id',)
      
admin.site.register(Event,EventAdmin)
admin.site.register(Status)
admin.site.register(EventEditorChoice,EditorChoiceAdmin)
