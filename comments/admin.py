from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    """ Comment Admin 정의 """

    list_display = (
        "user",
        "post",
        "content",
    )

    search_fields = (
        "^user__username",
        "^post__title",
    )