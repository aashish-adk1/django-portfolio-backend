from rest_framework import serializers
from .models import Photo
from .models import Video

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model=Photo
        fields='__all__'

    def get_image(self, obj):
     if obj.image:
        return obj.image.build_url(secure=True)
     return None 

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
        
class ContactSerializer(serializers.Serializer):
    PROJECT_TYPE_CHOICES = [
        ('wedding', 'Wedding Photography'),
        ('corporate', 'Corporate Event'),
        ('potrait', 'Potrait Session'),
        ('video', 'Video Production'),
        ('other', 'Other'),
    ]
    firstName=serializers.CharField(max_length=20)
    lastName=serializers.CharField(max_length=20)
    email=serializers.EmailField()
    project_type=serializers.ChoiceField(choices=PROJECT_TYPE_CHOICES)
    message=serializers.CharField()
