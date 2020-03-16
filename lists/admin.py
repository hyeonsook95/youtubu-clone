from django.contrib import admin
from .models import List


@admin.register(List)
class ListAdmin(admin.ModelAdmin):

    """ List Admin 정의 """

    list_display = (
        "creator",
        "name",
        "count_posts",
    )

    search_fields = (
        "^creator__username",
        "^name",
    )

