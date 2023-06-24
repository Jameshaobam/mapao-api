from django.shortcuts import render,HttpResponse
# # from .serializers import DiscoverSerializer,CategorySerializer,PostDiscoverSerializer,ReviewSerializer
from .models import Profile
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly ,AllowAny
from django.contrib.auth.models import User
import uuid,math,random


@api_view(["POST"])

def userRegister(req):
    try:
     print("Test")
     print(req.data)
     if not req.user.is_authenticated:
        print("allowed")
 
        user = User.objects.create_user(username=req.data["username"],password=req.data["password"],email=req.data["email"])
      #   profile = Profile.objects.create(user=user,username=user.username,email=user.email)
   
        return Response({
           "status":201,
           "detail":"Profile created!",
         #   "data":profile.id
        })
     else:

        print("Not allowed")
        return Response({
           "status":400,
           "detail":"Logout first"
        })
    except Exception as e:
        print("ERROR "+str(e))