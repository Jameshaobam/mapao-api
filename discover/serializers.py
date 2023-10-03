from rest_framework import serializers
from . models import Category,Discover,Review,DiscoverEditorChoice

#TODO FOR DISPLAY ONLY
class DiscoverSerializer(serializers.ModelSerializer):
    #TODO: SerializerMethodField() args ta method maming haptragana, get_method_name() hapkadaba
    # category_detail = serializers.SerializerMethodField("category_fn")
   
   #----------------------------------------------

   category_fn = serializers.SerializerMethodField()
   def get_category_fn(self,obj):
        return {
            "id":obj.category.id,
            "title":obj.category.name,
            "description":obj.category.description
        }
#     #TODO:SerializerMethodField() args yaobei method name da get hpparoi
   location = serializers.SerializerMethodField("location_detail")
   def location_detail(self,obj):
        return{
            "origin":obj.origin_location,
            "based":obj.based_location
        }
    
   

   likes = serializers.SerializerMethodField("like_count")
   def like_count(self,obj):
    return obj.like_set.all().count()
   
   like_url = serializers.SerializerMethodField("like_url_req")
   def like_url_req(self,obj):
       return f"http://127.0.0.1:8000/api/v1/discover/{obj.id}/like"
   

   poster = serializers.SerializerMethodField("poster_get")
   def poster_get(self,obj):
        return {
            "profile_id":obj.poster.id,
            "username":obj.poster.username
        }
   
   iseditorchoice = serializers.SerializerMethodField("editorchoice")
   def editorchoice(self,obj):
        return DiscoverEditorChoice.objects.filter(discover_item_id = obj.id).exists()
   
   #TODO: Getting context from views
   isowner = serializers.SerializerMethodField()
   def get_isowner(self,obj):
        
        return self.context.get("user_id") == obj.poster.user.id
   class Meta:
        model = Discover
        read_only_fields = ('id', 'created_time','likes','category_fn',"location","like_url","iseditorchoice") #Post twrkpada add twraroi read khk oirani
        fields = ["id","title","description","category_fn","location",
                  "likes","source_link","social_media_link","like_url",
                  "poster","iseditorchoice","isowner","logo"] #display twrani aduga Post twvada accept twgadaba fields khei
     

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        read_only_feilds = ('id',)
        fields=["id","name","description"]


#TODO: for posting only
class PostDiscoverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discover
        #Not accepting values from POST req 
        read_only_fields = ('id', 'created_time')
        #Post data twrkpada asigi fields khei siga manana twraga save twgadaba asida yaodaba twba yade
        fields = ["id","title","description","category","origin_location","based_location","source_link","social_media_link","poster","logo"]



class ReviewSerializer(serializers.ModelSerializer):

    reviewer = serializers.SerializerMethodField()
    def get_reviewer(self,obj):
        return {
            "profile_id":obj.reviewer.id,
            "username":obj.reviewer.username
        }

    class Meta:
        model = Review
        read_only_fields = ('id', 'created_time')
        fields = ["id","discover_item","review_description","created_time","reviewer"]