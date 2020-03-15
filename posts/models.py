from django.db import models
from core.models import TimeStampedModel

class Category(TimeStampedModel):

    """ Post의 Category Model 정의 """

    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name="sub_categories")

    def __str__(self):
        return f"{self.parent_category.name}/{self.name}"

    class Meta:
        ordering = ("name",)


class Post(TimeStampedModel):

    """ Post Model 정의 """

    creator = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, related_name="posts")
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, related_name="posts")
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to="post/thumbnails")
    video = models.FileField(upload_to="post/videos")
    