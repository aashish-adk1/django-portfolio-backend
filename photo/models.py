from django.db import models

# Create your models here.
class Photo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="photo/")
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Video(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    video=models.FileField(upload_to="video/")  
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
     
