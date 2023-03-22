from django.db import models
from myapp.storage import OverwriteStorage




   

class Account(models.Model):
    username=models.CharField(max_length=50)
    follower_count=models.IntegerField(null=True,default=0)
    following_count=models.IntegerField(null=True,default=0)
    post_count=models.IntegerField(null=True,default=0)
    followers = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)
    followings = models.ManyToManyField("self",related_name="folloing_by",symmetrical=False,blank=True)
    # requestsofuser=models.FileField(upload_to='Media', null=True)
    image = models.ImageField( max_length=25000, storage=OverwriteStorage(),upload_to='Media', null=True)
    
    text=models.CharField(max_length=1000,null=True,default="")
    date=models.DateTimeField(null=True)

    # def __str__(self):
    #     return self.name
class upimages(models.Model):
    username=models.CharField(null=True,max_length=50)
    images=models.ImageField(null=True,upload_to='Media')
    text=models.CharField(max_length=1000,null=True,default="")
    like_count=models.IntegerField(null=True,default=0 )
    dislike_count = models.IntegerField(null=True,default=0)

class likefeed(models.Model):
    username=models.CharField(max_length=50)
    like_id=models.CharField(max_length=20000)
    count=models.IntegerField(default=0)

class dislikefeed(models.Model):
    username=models.CharField(max_length=50)
    dislike_id=models.CharField(max_length=20000)
    count=models.IntegerField(default=0)
# Create your models here.
