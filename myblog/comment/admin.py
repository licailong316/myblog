from django.contrib import admin

from myblog.custom_site import custom_site
from .models import Comment
# from typeidea.base_admin import BaseOwnerAdmin


# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
