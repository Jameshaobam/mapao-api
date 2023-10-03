from rest_framework import serializers
from . models import Event,Status

#TODO FOR DISPLAY ONLY
class GetEventSerializer(serializers.ModelSerializer):
   
   going_number = serializers.SerializerMethodField("going_count")
   def going_count(self,obj):
    status_going = "G"
    return obj.status_set.all().filter(going=status_going).count()


   class Meta:
        model = Event
        #Post twrkpada add twraroi read khk oirani
        read_only_fields = ('id', 'created') 

        #display twrani aduga Post twvada accept twgadaba feild khei
        fields = [
            "id","title","description",
            "spot","state","date",
            "host","poster","created",
            "facebook","instagram","ticket",
            "image_url","host_phone_number",
            "going_number",
                  ] 
#TODO: FOR POSTING ONLY   
class PostEventSerializer(serializers.ModelSerializer):
   
      class Meta:
        model = Event
        read_only_fields = ('id', 'created') 
        fields = [
            "id","title","description",
            "spot","state","date",
            "host","poster","created",
            "facebook","instagram","ticket",
            "image_url","host_phone_number",
                  ] 