from django.contrib import admin
from .models import Category,Discover,Like,Review,DiscoverEditorChoice



class CategoryAdmin(admin.ModelAdmin):

        readonly_fields=('id',)


class DiscoverAdmin(admin.ModelAdmin):
        #TODO: admin CANNOT CHANGED THE INFO
        readonly_fields=('id','created_time')
        search_fields=('id','title','origin_location','based_location')
        
class LikeAdmin(admin.ModelAdmin):

        readonly_fields=('id','discover_item','liker')

class ReviewAdmin(admin.ModelAdmin):

        readonly_fields=('id',)

class EditorChoiceAdmin(admin.ModelAdmin):
        readonly_fields=('id',)
      
admin.site.register(Review,ReviewAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Discover,DiscoverAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(DiscoverEditorChoice,EditorChoiceAdmin)
