from django.db import models

# Create your models here.

class User(models.Model):

    gender = (
        ('male','男'),
        ('female','女'),
    )
    id = models.CharField(max_length=32,unique=True,primary_key=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ["-c_time"]
        verbose_name = '用户'
        verbose_name_plural = '用户'

class UserInfo(models.Model):
    id = models.OneToOneField(
         "User",
        
        on_delete=models.CASCADE,
        primary_key=True
        
    )
    
    temp = models.CharField(max_length=16)
    locat = models.CharField(max_length=32)
    locations = models.CharField(max_length=256)
    level = models.CharField(max_length=4)
    info = models.BooleanField(null=True)
    
    def __str__(self) -> str:
        return self.name
