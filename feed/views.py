from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Feed
from discover.models import Discover
from account.models import Profile
from .serializers import GETFeedSerializer,POSTFeedSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def allFeeds(req):
   feeds = Feed.objects.all()

   print(list(feeds))
   r = list(feeds)
   r.insert(3,feeds[0])
   
   serializer = GETFeedSerializer(r,many=True)
   return Response({

      "status":200,
      "data":serializer.data
   })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addFeed(req):

   try:
    user =  req.user
    data = req.data
    if user.is_authenticated :
      if len(data)<=0:
        return Response({
          "detail":"No data passed"
        })
      profile =Profile.objects.get(user_id=user.id)

      data.update({
        "poster":profile.id,
      })
      serializer = POSTFeedSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          "status":201,
          "detail":"Feed created"
        })
      else:
        print("Invalid data")
        return Response({
          "detail": "Invalid data"
        })
      

   except Exception as e:
     print(e)
