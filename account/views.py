from django.shortcuts import render,HttpResponse
# # from .serializers import DiscoverSerializer,CategorySerializer,PostDiscoverSerializer,ReviewSerializer
from .models import Profile
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly ,AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from .auth import get_token_for_user
from rest_framework import status

@api_view(["POST"])

def userRegister(req):
    try:
     print("Test")
     print(req.data)
     if not req.user.is_authenticated:
        print("allowed")
        user= User.objects.filter(username = req.data["username"]).exists()

        if(user):
           print("exist")
           user_obj = User.objects.get(username = req.data["username"])
  
           return Response({
           "status":401,
           "detail":"Profile with the username already exists",
   
        })
        else:
           print("not exist")
 
           user = User.objects.create_user(username=req.data["username"],password=req.data["password"],email=req.data["email"])
           
   
        return Response({
           "status":201,
           "detail":"Profile created!",
         #   "data":profile.id
        })
     else:

        print("Not allowed")
        return Response({
           "status":401,
           "detail":"Logout first"
        })

    
    except Exception as e:
        print("ERROR "+str(e))
        return Response({
           "status":401,
           "detail":"Error",
   
        })
    
@api_view(['GET'])

def isAuth(req):
   try:
      
      isUser = req.user
      isUserAuth = isUser.is_authenticated
      username = isUser.username
      userid = isUser.id
      print(isUser)
      profile = Profile.objects.get(user_id=userid)
      print(profile)
   except Profile.DoesNotExist:
      return Response({
      "is_authenticated":isUserAuth,
      "username":username,
      "userid":userid,

   })

   return Response({
      "is_authenticated":isUserAuth,
      "username":username,
      "userid":userid,
      "profileid":profile.id,
      "profilename":profile.username
   })


@api_view(['POST'])

def userLogin(req):

   data = req.data
   currentuser = req.user
   try:
    print(currentuser.is_authenticated)
    if currentuser.is_authenticated:
       return Response({
          "status":403,
          "detail":"Logout first"

       },status=status.HTTP_403_FORBIDDEN)
    user_name = data["username"]
    user_pass = data["password"]

    user =  authenticate(username = user_name,password=user_pass)
    if user is None:
       print("User with the credentials not found")

       return Response({
          "status":401,
          "detail":"User with the given credentials not found.Check the credentials again"
       },status=status.HTTP_401_UNAUTHORIZED)
    
    token = get_token_for_user(user)

    return Response(
       token, status=status.HTTP_200_OK
       )
   except Exception as e:
      print(e)
      return Response({
          "status":500,
          "detail":"Error has occurred in login"
       },status=status.HTTP_500_INTERNAL_SERVER_ERROR)