from django.http import JsonResponse
from .models import Profile
import json
from rest_framework_simplejwt.tokens import RefreshToken

def AuthUserCheck(rq):
   try:

      isUser = rq.user
      isUserAuth = isUser.is_authenticated
      username = isUser.username
      userid = isUser.id
      if isUser.is_authenticated:
       isuseradmin = isUser.is_staff
      
      profile = Profile.objects.get(user_id=userid)

   except Profile.DoesNotExist:
      return JsonResponse({
      "is_authenticated":isUserAuth,
      "username":username,
      "userid":userid,
      "isadmin":False

   })

   return JsonResponse({
      "is_authenticated":isUserAuth,
      "username":username,
      "userid":userid,
      "profileid":profile.id,
      "profilename":profile.username,
       "isadmin":isuseradmin
   })

def resToJson(response):
   return json.loads(response.content)
#manually generate token for login
def get_token_for_user(user):
   
   refresh = RefreshToken.for_user(user)
   
   return {
      "refresh":str(refresh),
      "access": str(refresh.access_token),
      "userid":user.id
   }

