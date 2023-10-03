from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .serializers import DiscoverSerializer, CategorySerializer, PostDiscoverSerializer, ReviewSerializer
from .models import Category, Discover, Like, Review, DiscoverEditorChoice
from account.models import Profile
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import status
from account.auth import AuthUserCheck, resToJson


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticatedOrReadOnly])
def getDiscovers(req):
    try:
        if req.method == "GET":
            discoveries = Discover.objects.all().filter(
                is_deleted=False).order_by("-created_time")
            serializer = DiscoverSerializer(
                # context to pass arguments to serializer class
                discoveries, many=True, context={'user_id': req.user.id}
            )

            return Response(
                {
                    "status": 200,
                    "datas":  serializer.data,

                }

            )

        # TODO POST DISCOVER
        if req.user.is_authenticated:
            print(req.data)
            profile = Profile.objects.get(user_id=req.user.id)
            print(profile)
            req.data.update({
                "poster": profile.id
            })
            serializer = PostDiscoverSerializer(data=req.data)
            print(serializer)

            if serializer.is_valid():
                serializer.save()
                print("SAVED")
            else:
                print("Invalid")
                print(serializer.errors)
                return Response({
                    "status": 500,
                    "detail": "Error! post not created Invalid",
                    "data": []
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({"detail": "created", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response({"detail": "Not authenticated", "status": 401}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(e)

        return Response({
            "status": 500,
            "detail": "Error! post not created",
            "data": []
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateDiscover(req, disc_id):
    try:

        discover = Discover.objects.get(id=disc_id, is_deleted=False)
        # TODO POST DISCOVER
        if req.user.is_authenticated and req.user.id == discover.poster.user.id:

            serializer = PostDiscoverSerializer(
                instance=discover, data=req.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                print("SAVED")
            else:
                print("Invalid")
                return Response({
                    "detail": "Error! post not updated"
                })

            return Response({"detail": "Updated", "data": serializer.data})

        return Response({"detail": "Not authenticated Or Not allowed this action", "status": 401})

    except Discover.DoesNotExist:
        return Response({"detail": "Discover item not exist", "status": 404, "data": []})
    except Exception as e:
        print(e)

        return Response({
            "detail": "Error! post not created",
            "data": []
        })


@api_view(["GET"])
def getCategories(req):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(
        {
            "status": 200,
            "datas":  serializer.data,

        }

    )


@api_view(["GET"])
def getCategorizedDiscoveries(req):

    try:
        values = req.GET
        print(values)
        cat_id = values["cat"]
        discoveries = Discover.objects.filter(
            category_id=cat_id, is_deleted=False).order_by("-created_time")
        if discoveries.count() <= 0:
            print("No datas")
    except Exception as e:

        print(e)

        return Response({
            "log": "error on getting datas"
        })

    serializer = DiscoverSerializer(discoveries, many=True)
    return Response(
        {
            "status": 200,
            "datas":  serializer.data,
        }
    )


@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def getDetailDiscover(req, disc_id):
    try:
        discover = Discover.objects.get(id=disc_id, is_deleted=False)
        print(discover.poster.user.id)
        user = req.user
        print(user.id)
        profile = Profile.objects.get(user_id=user.id)
        # isyou = user.id == discover.poster.user.id
        isLiked = Like.objects.filter(
            discover_item_id=discover.id, liker_id=profile.id).exists()
        print(discover.poster)

        serializer = DiscoverSerializer(
            discover, many=False, context={'user_id': req.user.id})
        reviews = discover.review_set.all()
        review_serializer = ReviewSerializer(reviews, many=True)

    except Discover.DoesNotExist:
        print("Discover not exist")
        return Response({
            "status": 404,
            "detail": "Item not found",
            "data": []
        })
    except Exception as e:
        print(e)

        return Response({
            "status": 404,
            "detail": "Some error occured ",
            "data": []
        })

    return Response({

        "liked": isLiked,
        "status": 200,
        "detail": "Working",
        "data": serializer.data,
        "reviews": review_serializer.data,

    })


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def likeDiscover(req, disc_id):
    status = 201
    detail = ""
    likeCount = -1
    try:
        if req.user.is_authenticated:
            discover = Discover.objects.get(id=disc_id, is_deleted=False)
            profile = Profile.objects.get(user_id=req.user.id)
            like_obj = Like.objects.get(
                discover_item_id=discover.id, liker_id=profile.id)
            print(like_obj)
            like_obj.delete()
            detail = "Like removed"
            likeCount = discover.like_set.all().count()
            # obj.like_set.all().count()

        else:
            status = 404
            detail = "Not authenticated"
    except Profile.DoesNotExist:
        print("Profile does  not found")
        status = 404
        detail = "Profile does not found"
    except Like.DoesNotExist:
        print("Like object not found")
        like = Like.objects.create(
            discover_item=discover,
            liker=profile
        )
        likeCount = discover.like_set.all().count()
        print(f"Like count {likeCount}")
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
                "status": status,
                "detail": detail,
                "likeCount": likeCount
            }
        )


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteDiscover(req, disc_id):
    try:
        discover = Discover.objects.get(id=disc_id, is_deleted=False)
        if req.user.is_authenticated and not discover.is_deleted == True and discover.poster.user.id == req.user.id:
            print("authenticatd")
            discover.is_deleted = True
            discover.save()
        else:
            return Response({
                "status": 401,
                "detail": "Not authenticated or allowed to perform this action"
            }, status=status.HTTP_401_UNAUTHORIZED)

    except Discover.DoesNotExist:
        return Response({
            "status": 404,
            "detail": "Discover item not found"
        }, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        print(e)
        return Response({
            "status": 500,
            "detail": "Error has occured"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({
        "status": 200,
        "detail": "Discover item deleted"
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addReview(req, disc_id):
    try:
        discover = Discover.objects.get(id=disc_id)
        profile = Profile.objects.get(user_id=req.user.id)
        data = req.data
        print(data)
        Review.objects.create(
            discover_item=discover,
            review_description=data["description"],
            reviewer=profile
        )
    except Discover.DoesNotExist:
        print("Discover not found")
        return Response({

        })
    except Profile.DoesNotExist:
        print("Profile not found")
        return Response({

        })
    except Exception as e:
        print("Exception has occured " + str(e))
        return Response({

        })

    return Response({
        "status": 201,
        "detail": "Review added"
    })


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteReview(req, review_id):
    try:
        review = Review.objects.get(id=review_id)
        if req.user.is_authenticated and review.reviewer.user.id == req.user.id:
            review.delete()
           
            return Response({
                "status": 200,
                "detail": "Deleted"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "status": 401,
                "detail": "Not authenticated or allowed to perform this action"
            }, status=status.HTTP_401_UNAUTHORIZED)

    except Review.DoesNotExist:
        return Response({
            "status": 404,
            "detail": "Review item not found",

        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({
            "status": 500,
            "detail": "Error has occured"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def makeEditorChoice(req, disc_id):
    user_response = AuthUserCheck(req)
    user_data = resToJson(user_response)
    try:
        if user_data["isadmin"] == True:
            discover = Discover.objects.get(id__exact=disc_id)
            discovereditor = DiscoverEditorChoice.objects.filter(
                discover_item_id__exact=disc_id)
            print(len(discovereditor))
            profile = Profile.objects.get(id__exact=user_data["profileid"])

            print(profile)
            if len(discovereditor) <= 0:
                DiscoverEditorChoice.objects.create(
                    discover_item=discover,
                    admin=profile
                )
                return Response({
                    "status": 201,
                    "detail": f"{disc_id} has made editor choice"
                })
            else:
                return Response({
                    "status": 400,
                    "detail": f"{disc_id} has already in editor choice"
                })

        else:
            return Response({
                "status": 400,
                "detail": "Not allowed to perform the action,Try as admin"
            })
    except Discover.DoesNotExist:
        return Response({
            "status": 404,
            "detail": "Discover object not found"
        })
    except Exception as e:
        print(e)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMyDiscoveries(req):

    try:
        user = req.user
        if user.is_authenticated:
            # use double underscore -- to traverse the multiple related foreign keys
            discoveries = Discover.objects.filter(
                is_deleted=False, poster__user__id=user.id).order_by("-created_time")
            serializer = DiscoverSerializer(
                # context to pass arguments to serializer class
                discoveries, many=True, context={'user_id': req.user.id}
            )
            return Response(
                {
                    "status": 200,
                    "detail": "Working",
                    "datas": serializer.data
                }, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "status": 401,
                    "detail": "Not authenticated",

                }, status=status.HTTP_401_UNAUTHORIZED
            )
    except Exception as e:
        print(e)
        return Response(
            {
                "status": 500,
                "detail": "Error on fetching data",
                "datas": []
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
