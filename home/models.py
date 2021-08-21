from django.db import models
from core.model import *
from Accounts.models import *

# Create your models here.

class trekcategory(BaseModel):
    category_name = models.CharField(max_length=100)
    category_desc = models.CharField(max_length=500)
    cattegory_image = models.ImageField(upload_to ='category-image')

    def __str__(self):
        return self.category_name
    class Meta:
        ordering =['-created_at']

class Treck(BaseModel):
    treckcat= models.ForeignKey(trekcategory, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=1000)
    long_desc = models.TextField()
    days = models.CharField(max_length=20, null=True, blank=True)
    distance = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    image= models.ImageField(upload_to ='treck-image')
    
    class Meta:
        ordering =['created_at']    



    
class Itinerary (BaseModel):
    treck = models.ForeignKey(Treck, on_delete=models.CASCADE)
    Sitinerary = models.CharField(max_length= 200)
    


class Treck_Image(BaseModel):
    treckimg = models.ForeignKey(Treck, on_delete=models.CASCADE)
    treckimage = models.ImageField(upload_to= 'trecks/treckname')
    class Meta:
        ordering =['-created_at']

class review(BaseModel):
    ureview = models.ForeignKey(usersignup, on_delete=models.CASCADE, null=True, blank=True)
    treckreview = models.ForeignKey(Treck, on_delete=models.CASCADE, null=True, blank=True)
    reviews = models.TextField()
    review_number = models.IntegerField( default='0' ,null=True,blank=True)


class Boodtreck(BaseModel):
    userbookid=models.ForeignKey(usersignup, on_delete=models.CASCADE)
    treckid = models.ForeignKey(Treck, on_delete=models.CASCADE)
    bookname = models.CharField(max_length=100,null=True,blank=True)
    bookemail = models.CharField( max_length=254)
    booknumber = models.CharField(max_length=13)
    bookaddress = models.TextField()
    booknotes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.bookemail


class blogmodel(BaseModel):

    blogTitle = models.CharField(max_length=100)
    blogcontent = models.TextField()
    blogimage = models.ImageField(upload_to='blogimage')

    def __str__(self):
        return self.blogTitle

    class Meta:

        ordering =['-created_at']    
    




    