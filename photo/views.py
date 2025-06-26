from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PhotoSerializer,VideoSerializer,ContactSerializer
from .models import Photo,Video
from django.core.mail import send_mail
from django.conf import settings

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
    
    
class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            firstName = serializer.validated_data['firstName']
            lastName = serializer.validated_data['lastName']
            email = serializer.validated_data['email']
            project_type = serializer.validated_data['project_type']
            message = serializer.validated_data['message']

            subject = f"New Contact: {project_type} project from {firstName} {lastName}"
            body = (
                f"Name: {firstName} {lastName}\n"
                f"Email: {email}\n"
                f"Project Type: {project_type}\n\n"
                f"Message:\n{message}"
            )

            try:
                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                return Response({'detail': 'Message sent successfully'}, status=200)
            except Exception as e:
                return Response({'detail': f'Error sending email: {str(e)}'}, status=500)
        else:
            return Response(serializer.errors, status=400)