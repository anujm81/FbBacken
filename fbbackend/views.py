# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from all_serializers import UserSerializer, FriendSerializer, MsgSerializer, CommentSerializer

from fbbackend.models import Friend, Messages, FriendshipRequest, Comments


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



@api_view(['POST'])
def getAllFrnds(request):
    user_id = request.data['user_id']
    print user_id
    allFrnds = Friend.objects.filter(to_user = user_id)
    arr1 = []
    arr2 = []
    for frnd in allFrnds:
        arr2.append(frnd.from_user)
    serializer2 = UserSerializer(arr2, many=True)

    return Response(JSONRenderer().render(serializer2.data))

@api_view(['POST'])
def getAllMsgs(request):
    user_id = request.data['user_id']
    allMsgs = Messages.objects.filter(mess_to_user = user_id)
    arr1 = []
    arr2 = []

    for msg in allMsgs:
        arr1.append(msg)
        arr2.append(msg.mess_from_user)
    serializer1 = FriendSerializer(arr2, many=True)
    serializer2 = MsgSerializer(arr1, many = True)

    return Response(JSONRenderer().render(serializer2.data + serializer1.data))

@api_view(['POST'])
def getAllFrndRequest(request):
    user_id = request.data['user_id']
    allRequests = FriendshipRequest.objects.filter(to_user = user_id)
    arr1 = []
    for request in allRequests:
        arr1.append(request.from_user)
    serializer = FriendSerializer(arr1, many = True)
    return Response(JSONRenderer().render(serializer.data))

@api_view(['POST'])
def getAllComments(request):
    user_id = request.data['post_id']
    allComments = Comments.objects.filter(post=user_id)
    arr1 = []
    arr2 = []
    for comment in allComments:
        arr1.append(comment.from_user)
        arr2.append(comment)
    serializer1 = FriendSerializer(arr1, many=True)
    serializer2 = CommentSerializer(arr2, many=True)
    return Response(JSONRenderer().render(serializer1.data + serializer2.data))


