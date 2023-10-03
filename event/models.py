from django.db import models
from account.models import Profile

class Event (models.Model):
    title = models.CharField(max_length=100,blank=False,null=False)
    description = models.TextField(blank=False,null=False)
    spot = models.CharField(max_length=300,blank=False,null=False)
    state=models.CharField(max_length=200,blank=False,null=False)
    date = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    facebook = models.CharField(max_length=350, blank=True,null=True)
    instagram = models.CharField(max_length=350,blank=True,null=True)
    ticket = models.CharField(max_length=350,blank=True,null=True)
    image_url = models.CharField(max_length=500,blank=True,null=True)
    host_phone_number = models.CharField(max_length=10,blank=False,null=False)
    is_deleted = models.BooleanField(default=False,blank=False,null=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        
    def __str__(self):
        return "{0}||{1}||{2}".format(self.title,self.spot,self.state)

class Status (models.Model):
    status_going = "G"
    status_not_going="N"
    status = (
        (status_going,"Going"),
        (status_not_going,"Not Going"),
    )

    going = models.CharField(max_length=1,choices=status,blank=False,null=False)
    person = models.ForeignKey(Profile,on_delete=models.CASCADE)
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
        
    def __str__(self):
        return "{0}||{3}||{1}||{2}".format(self.id,self.person.id,self.event.title,self.going)

class EventEditorChoice(models.Model):
    event_item = models.ForeignKey(Event,on_delete=models.CASCADE)
    admin = models.ForeignKey(Profile,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.event_item} || {self.admin} || {self.id}"
    

