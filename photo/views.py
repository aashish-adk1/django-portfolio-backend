from rest_framework import generics
from .serializers import PhotoSerializer,VideoSerializer
from .models import Photo,Video

# Create your views here.
class PhotoListView(generics.ListAPIView):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer

class PhotoCreateView(generics.CreateAPIView):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer
    
    
class PhotoUpdateView(generics.UpdateAPIView):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer
    lookup_field='id'
    
    
class PhotoDeleteView(generics.DestroyAPIView):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer
    lookup_field='id'
    
    
class VideoListView(generics.ListAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer


class VideoCreateView(generics.CreateAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer


class VideoUpdateView(generics.UpdateAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
    lookup_field='id'


class VideoDeleteView(generics.DestroyAPIView):
    queryset=Video.objects.all()
    serializer_class=VideoSerializer
    lookup_field='id'