from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class home_insert(models.Model):
    home_title = models.CharField(max_length=50)
    home_slogan = models.CharField(max_length=50)
    home_pic = models.FileField(upload_to="adminPanel/", max_length=250,null=True,default=None)
    # home_pic = models.ImageField(upload_to='home/',blank=True,null=True)

class sub_home_insert(models.Model):
    short_title = models.CharField(max_length=20)
    sub_short_title = models.CharField(max_length=20)
    home_pic = models.FileField(upload_to="adminPanel/", max_length=250,null=True,default=None)
