from django.contrib import admin
from django.utils.html import mark_safe

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    """ Post Admin 정의 """

    list_display = (
        "creator",
        "category",
        "title",
        "get_thumbnail",
    )

    list_filter = ("category",)

    search_fields = (
        "^user__username",
        "^title",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.thumbnail.url}"/>')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    """ Category Admin 정의 """

    list_display = ("__str__",)
