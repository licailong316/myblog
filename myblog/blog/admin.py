from django.contrib.admin.models import LogEntry
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from myblog.base_admin import BaseOwnerAdmin
from myblog.custom_site import custom_site
from .models import Post, Category, Tag


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message')


class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count', 'owner')
    fields = ('name', 'status', 'is_nav',)

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'owner')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    """ 自定义过滤器只展示当前用户分类 """

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post)
class PostAdmin(BaseOwnerAdmin):
    list_display = ['title', 'category', 'status', 'created_time', 'operator', 'owner']
    list_display_links = []

    list_filter = [CategoryOwnerFilter, ]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = False

    exclude = ('owner',)

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': ('title', 'category', 'status'),
        }),
        ('内容', {
            'fields': ('desc', 'content'),
        }),
        ('额外信息', {
            # 'classes': ('collapse',),
            'fields': ('tag',),
        })
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,)),
        )

    operator.short_description = '操作'
