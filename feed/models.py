from django.db import models
from account.models import Profile
import time


class Feed(models.Model):
    type_discover = "D"
    type_event = "E"
    type_untold = "U"
    type_feed = "F"
    types = (
        (type_discover, "Discover"),
        (type_event, "Event"),
        (type_untold, "Untold"),
        (type_feed, "Feed"),
    )

    headline = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=500, blank=False, null=False)
    image_url = models.CharField(max_length=500, blank=False, null=False)
    source = models.CharField(max_length=500, blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    feed_type = models.CharField(max_length=1,choices=types,default=type_feed)
    related_id = models.CharField(max_length = 20,blank=True,null=True)
    logo= models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return f"{self.headline}||{self.feed_type}||{self.id}"