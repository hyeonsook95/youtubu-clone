from django.db import models
from core.models import TimeStampedModel


class List(TimeStampedModel):

    """ List Model 정의 """

    creator = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, related_name="lists"
    )
    name = models.CharField(max_length=50)
    post = models.ManyToManyField("posts.Post", related_name="lists")

    def count_posts(self):
        post = self.posts.all().count()
        return post
