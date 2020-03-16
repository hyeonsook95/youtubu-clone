from django.db import models
from core.models import TimeStampedModel


class Channel(TimeStampedModel):

    """ Channel Model 정의 """

    creator = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, related_name="channels"
    )
    name = models.CharField(max_length=50)
    art = models.ImageField(upload_to="channels")

    """
    def count_subscribes(self):
        subscribe = self.subscribes.all().count()
        return subscribe
    """
