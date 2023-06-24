from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .serializers import DiscoverSerializer,CategorySerializer,PostDiscoverSerializer,ReviewSerializer
from .models import Category,Discover,Like,Review
from .models import Profile
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly ,AllowAny

@api_view(["GET","POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def getDiscovers(req):
  try:
    if req.method == "GET":
        discoveries = Discover.objects.all().filter(is_deleted=False).order_by("-created_time")
        serializer = DiscoverSerializer(discoveries,many=True)
        return Response(
            {
                "status":200,
                "datas":  serializer.data,
                
            }    
        )
    if req.user.is_authenticated:
        print(req.data)
        profile=Profile.objects.get(user_id=req.user.id)
        print(profile)
        req.data.update({
            "poster":profile.id
        })
        serializer = PostDiscoverSerializer(data=req.data)
        print(serializer)
        
        if serializer.is_valid():
            serializer.save()
            print("SAVED")
        else:
            print("Invalid")
            return Response({
                "detail":"Error! post not created"
            })

        

        return Response({"detail": "created", "data": serializer.data})
    
    return Response({"detail": "Not authenticated", "status":404})
  except Exception as e:
      print(e)

      return Response({
                "detail":"Error! post not created",
                "data":str(e)
            })


@api_view(["GET"])
def getCategories(req):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return Response(
        {
            "status":200,
            "datas":  serializer.data,
            
        }
    
    )

@api_view(["GET"])

def getCategorizedDiscoveries(req,cat_id):
   
    try:
      discoveries = Discover.objects.filter(category_id=cat_id,is_deleted=False).order_by("-created_time")
      if discoveries.count()<=0:
          print("No datas")
    except Exception as e:
            
           print(e)

           return Response({
               "log":"error on getting datas"
           })
    

    serializer = DiscoverSerializer(discoveries,many=True)
    return Response(
        {
            "status":200,
            "datas":  serializer.data,
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def getDetailDiscover(req,disc_id):
    try:
        discover =  Discover.objects.get(id=disc_id,is_deleted=False)
        print(discover.poster.user.id)
        print(req.user.id)
        if  not req.user.is_authenticated or not req.user.id == discover.poster.user.id: #discover.poster.user.id
            return Response({
            "status":404,
            "detail":"Not authenticated"
        })
        
        print(discover.poster)
        print(req.user.id == discover.poster.user.id)
        serializer = DiscoverSerializer(discover,many=False)
        reviews =  discover.review_set.all()
        review_serializer =  ReviewSerializer(reviews,many=True)

    except Discover.DoesNotExist:
        print("Discover not exist")
        return Response({
            "status":404,
            "detail":"Item not found"
        })
    except Exception as e:
        print(e)

        return Response({
                "status":404,
                "detail":"Some error occured "
            })
    
    return Response({
        "status":200,
        "detail":"Working",
        "data":serializer.data,
        "reviews":review_serializer.data,

    })

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def likeDiscover(req,disc_id):
    status =201
    detail = ""
    try:
     if req.user.is_authenticated:
        discover = Discover.objects.get(id=disc_id,is_deleted=False)
        like_obj = Like.objects.get(discover_item_id = discover.id)
        print(like_obj)
        like_obj.delete()
        detail = "Like removed"
    
     else:
         status =404
         detail="Not authenticated"

    except Like.DoesNotExist:
        print("Like object not found")
        like = Like.objects.create(
         discover_item = discover
     )
        status = 201
        detail = "Liked created"
        
    except Discover.DoesNotExist:
        print("Discover not found")
        status = 404
        detail = "Discover object does'nt exists"

    except Exception as e:
        print(e)
        status = 404
        detail = "Error has occured"
    finally:

        return Response(
            {
                "status":status,
                "detail":detail
            }
        )
    

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def deleteDiscover(req,disc_id):
    try:
        discover = Discover.objects.get(id = disc_id,is_deleted=False)
        if req.user.is_authenticated and not discover.is_deleted == True and discover.poster.user.id == req.user.id:
            print("authenticatd")
            discover.is_deleted = True
            discover.save()
        else :
             return Response({
            "status":404,
            "detail":"Not authenticated"
        })
        
        
    except Discover.DoesNotExist:
        return Response({
            "status":404,
            "detail":"Discover item not found"
        })
    
    except Exception as e:
        print(e)
        return Response({
            "status":404,
            "detail":"Error has occured"
        })

    return Response({
        "status":201,
        "detail":"Discover item deleted"
    })
    