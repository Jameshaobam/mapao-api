from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .serializers import GetEventSerializer,PostEventSerializer
from .models import Status,Event
from account.auth import  AuthUserCheck,resToJson
from account.models import Profile
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly ,AllowAny

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def setGoing(req,event_id):
    try:
        event = Event.objects.get(id=event_id,is_deleted=False)
        profile = Profile.objects.get(user_id = req.user.id)
        status_check_object =  Status.objects.get(event=event,person=profile)
        status_check_object.delete()
        print("status deleted")
        return Response({
           "status":201,
           "detail":"Deleted",
        })
    except Status.DoesNotExist:
        status_going = "G"
        status_not_going="N"
        status_obj = Status.objects.create(
            going = status_going,
            person = profile,
            event = event
        )
        print(status_obj,sep="--")
        return Response({
           "status":201,
           "detail":"Marked going",
        })
    except Event.DoesNotExist:
        return Response({
           "status":404,
           "detail":"Event doesnt exists",
        })
    except Exception as e:
     print(e)


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])

def allEvents(req):
   try:
    values_param = req.GET
    response =  AuthUserCheck(req)
    data =resToJson(response)
    if values_param["state"].lower() == "all":
       events = Event.objects.filter(is_deleted=False)
    else:
       events = Event.objects.filter(state = values_param["state"].lower(),is_deleted=False)
    if events.count() <= 0:
           return Response({
            "auth":data,
            "status":200,
            "detail":"Events not found",
            "datas":[],
            })
    
    serializer =  GetEventSerializer(events,many=True)
    
    return Response({
            "auth":data,
            "status":200,
            "detail":"Working",
            "datas":serializer.data,
            })

   except Exception as e:
      print(e)
      return Response({
            "auth":data,
            "status":404,
            "detail":"Error has occured in fetching the datas",
            "datas":[]
            })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def postEvent(req):
   try:
      if req.user.is_authenticated:
         body = req.data
         user = req.user
         profile=Profile.objects.get(user_id=user.id)
         body.update({
            "poster": profile.id
         })
         serializer = PostEventSerializer(data=req.data)
         if serializer.is_valid():
            serializer.save()
            print("SAVED")
         else:
            print("Invalid")
            return Response({
          "status":401,
                "detail":"Error! post not created",
                "data":[]
            })

         return Response({"detail": "Event created", "data": serializer.data})
      
   except Exception as e:
      print(e)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateEvent(req,event_id):
   try:
      event = Event.objects.get(id=event_id,is_deleted = False)
      user = req.user
      if user.is_authenticated and event.poster.user.id == user.id:
   
         serializer = PostEventSerializer(instance=event,data=req.data,partial=True)

         if serializer.is_valid():
            serializer.save()
            print("SAVED")
         else:
            print("Invalid")
            return Response({
          "status":401,
                "detail":"Error! event not updated",
                "data":[]
            })

         return Response({"detail": "Event updated", "data": serializer.data})
      return Response({"detail": "Not authenticated Or Not allowed this action", "status":401})
    
   except Event.DoesNotExist:
      print("Event not exist")
      return Response({
          "status":401,
                "detail":"Error! event not updated",
                "data":[]
            })

   except Exception as e:
      print(e)
      return Response({
          "status":401,
                "detail":"Error! event not updated",
                "data":[]
            })
   
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteEvent(req,event_id):
   try:
      user = req.user

      event = Event.objects.get(id=event_id,is_deleted = False)
      if  user.id == event.poster.user.id:
         event.is_deleted = True
         event.save()
         return Response({
            "status":201,
            "detail":f"{event.title} is deleted"
         })
      return Response({
         "status":401,
         "detail":"Not authorized or authenticate to perform this action"
      })
   except Event.DoesNotExist:
      print("Event not exist")
      return Response({
         "status":404,
         "detail":"Event does not exist"
      })
   
   except Exception as e:
      print(e)
      return Response({
         "status":401,
         "detail":"Error in deleting event"
      })

