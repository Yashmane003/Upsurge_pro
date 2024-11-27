from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipt(models.Model):
        Fname=models.CharField(max_length=100,null=True)
        Lname=models.CharField(max_length=100,null=True)
        Email=models.CharField(max_length=100,null=True)
        Password=models.CharField(max_length=100,null=True)
        Course=models.CharField(max_length=100,null=True)
        Duration=models.CharField(max_length=100,null=True)
        # phone=request.POST.get("Phone")
        Address=models.CharField(max_length=100,null=True)
        City=models.CharField(max_length=100,null=True)
        Zipcode=models.CharField(max_length=100,null=True)

        user=models.ForeignKey(User,related_name="receipt", on_delete=models.DO_NOTHING)

        def __str__(self):
                return self.Fname