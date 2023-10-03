from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import DiscoverEditorChoice
from feed.models import Feed


def createDisECFeed(sender,instance,created,**kwargs):
    try:
        if created:
            editor = instance
            discover = editor.discover_item
            Feed.objects.create(
                headline = discover.title,
                description = discover.description,
                source = discover.source_link,
                image_url = "",
                poster = discover.poster,
                feed_type = "D",
                related_id = discover.id,
                logo = discover.logo

            )
    except Exception as e:
        print("error on signal "+str(e))

def deleteFeed(sender,instance,**kwargs):
    try:
        editor = instance
        feed = Feed.objects.get(related_id = editor.discover_item.id)
        feed.delete()
    except Exception as e:
        print("Error on delete signal "+str(e))

post_save.connect(createDisECFeed,sender=DiscoverEditorChoice)
post_delete.connect(deleteFeed,sender=DiscoverEditorChoice)