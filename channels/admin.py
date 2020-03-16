from django.contrib import admin
from .models import Channel


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):

    """ Channel Admin 정의 """

    list_display = (
        "creator",
        "name",
    )

    search_fields = (
        "^creator__username",
        "^name",
    )
