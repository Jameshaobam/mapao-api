from django.db import models
from django.contrib.auth.models import User
from account.models import Profile

class Category (models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250,null=True,blank=True)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name} {self.id}"
    

class Discover(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    origin_location = models.CharField(max_length=150)
    based_location = models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    source_link = models.CharField(max_length=300,null=True,blank=True)
    social_media_link = models.CharField(max_length=300,null=True,blank=True)
    is_deleted = models.BooleanField(default=False,)
    created_time = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(Profile,on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Discover"
        verbose_name_plural = "Discoveries"

    def __str__(self):
        return f"{self.title} {self.id}" 

class Like(models.Model):
    discover_item = models.ForeignKey(Discover,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self) -> str:
        return f"{self.id}|{self.discover_item.title}"
    
class Review(models.Model):
    discover_item = models.ForeignKey(Discover,on_delete=models.CASCADE)
    review_description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self) -> str:
        return f"{self.id}|{self.discover_item.title}"

