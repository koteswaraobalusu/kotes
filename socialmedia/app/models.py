from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
import uuid
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    userid=models.IntegerField()
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    
    address=models.CharField(max_length=100)
    image=models.FileField(upload_to="Profile_images",default="blank.jpg")
    def __str__(self):
        return self.first_name
class Post(models.Model):
    post_id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    userid=models.IntegerField()
    post_name=models.CharField(max_length=1000)
    post_image=models.FileField(upload_to="post_images")
    date=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)

class Likepost(models.Model):
    post_id=models.CharField(max_length=1000)
    username=models.CharField(max_length=100)
    def __str__(self):
        return self.username

