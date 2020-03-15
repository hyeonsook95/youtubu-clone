from django.db import models

from core.models import TimeStampedModel
from core.models import data_upload_to as upload_to
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Category(TimeStampedModel):

    """ Post의 Category Model 정의 """

    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="sub_categories")

    def __str__(self):
        
        if self.parent_category:
            return f"{self.parent_category.name}/{self.name}"
        else:
            return f"{self.name}"

    class Meta:
        ordering = ("name",)


class Post(TimeStampedModel):

    """ Post Model 정의 """

    creator = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, related_name="posts")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name="posts", null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    thumbnail = ProcessedImageField(upload_to="posts", processors=[ResizeToFill(295, 165)], format='JPEG', options={'quality': 60})
    video = models.FileField(upload_to="posts")


    



    
    