from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from video.models import Video
from video.sserializers import VideoSerializer


# Create your views here.
from rest_framework.authentication import SessionAuthentication

# class CsrfExemptSessionAuthentication(SessionAuthentication):
#     def enforce_csrf(self, request):
#         pass



# class VideoAPI(APIView):
#     authentication_classes = [CsrfExemptSessionAuthentication]
#     def post(self, request, format=None):
#         serializer = VideoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request, format=None):
#         videos = Video.objects.all()
#         serializer = VideoSerializer(videos, many=True)
#         return Response(serializer.data)
#

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
