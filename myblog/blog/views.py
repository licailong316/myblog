from django.shortcuts import render

from blog.models import Tag, Post, Category
from config.models import SideBar


# Create your views here.
def post_list(request, category_id=None, tag_id=None):
    #     tag = None
    #     category = None

    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_lists = []
        else:
            post_lists = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_lists = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_lists = post_lists.filter(category_id=category_id)
            # try:
            #     category = Category.objects.get(id=category_id)
            # except Category.DoesNotExist:
            #     category = None
            # else:
            #     post_lists = post_lists.filter(category_id=category_id)

    # context = {
    #     'category': category,
    #     'tag': tag,
    #     'post_list': post_lists,
    # }

    return render(request, 'blog/list.html', context={'post_list': post_lists})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    #
    # context = {
    #     'post': post,
    #     'sidebars': SideBar.get_all(),
    # }
    # context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context={'post': post})
