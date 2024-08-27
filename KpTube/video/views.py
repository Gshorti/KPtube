from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from video.models import Video
from video.sserializers import VideoSerializer

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']