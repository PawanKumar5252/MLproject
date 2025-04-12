from django.db import models

# Create your models here.
from django.utils import timezone

class Users(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.EmailField()
    upassword=models.CharField(max_length=15)

    class Meta:
        db_table = "users"
        # app_label = "users"


# class Fir(models.Model):
#     name=models.CharField(max_length=100)
#     gender=models.CharField(max_length=100)
#     age=models.IntegerField(max_length=100)
#     pincode=models.IntegerField(max_length=100)
#     mnumber=models.IntegerField(max_length=100)
#     address=models.CharField(max_length=100)
#     aadhaar=models.IntegerField(max_length=100)
#     poffice=models.CharField(max_length=100)
#     distric=models.CharField(max_length=100)
#     country=models.CharField(max_length=100)

#     class Meta:
#         db_table = "fir"



# class Fir_num(models.Model):
#     fir_number=models.IntegerField()
#     categories=models.CharField(max_length=10)
#     cause=models.TextField(max_length=400)
#     upload_to='staticfiles/images'
#     mig = models.ImageField(db_column='Image', upload_to='staticfiles/images', blank=True, null=True)   

#     class Meta:
#         db_table = "fir_num"



    def __str__(self):
        return self.name    