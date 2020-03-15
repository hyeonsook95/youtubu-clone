import os
from uuid import uuid4

from django.db import models


def data_upload_to(instance, filename):
    
    """ 미디어 파일의 이름을 hex 값으로 변경한다. """

    uuid_name = uuid4().hex[:20]
    extension = os.path.splitext(filename)[-1].lower()
    return f'{uuid_name}{extension}'


class TimeStampedModel(models.Model):

    """ TimeStamped Model """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True