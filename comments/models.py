from django.db import models
from core.models import TimeStampedModel


class Comment(TimeStampedModel):

    """ Comment Model 정의 """

    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, related_name="comments")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="comments")
    parent_comment = models.ForeignKey("Comment", on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    content = models.TextField()
