from django.contrib import admin
from .models import Category,Discover,Like,Review



class CategoryAdmin(admin.ModelAdmin):

        readonly_fields=('id',)


class DiscoverAdmin(admin.ModelAdmin):
        #TODO: admin CANNOT CHANGED THE INFO
        readonly_fields=('id','created_time','is_deleted','title','description','origin_location','based_location','category','social_media_link','source_link')
        search_fields=('id','title','origin_location','based_location')
        
class LikeAdmin(admin.ModelAdmin):

        readonly_fields=('id',)

class ReviewAdmin(admin.ModelAdmin):

        readonly_fields=('id',)
      
admin.site.register(Review,ReviewAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Discover,DiscoverAdmin)
admin.site.register(Like,LikeAdmin)

