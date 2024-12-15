"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from comment.views import CommentView
# from blog.views import post_list, post_detail
from config.views import LinkListView
from myblog.custom_site import custom_site
from blog.views import PostDetailView, IndexView, CategoryView, TagView, SearchView, AuthorView
from django.contrib.sitemaps import views as sitemap_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),  # 对应首页
    path('category/<int:category_id>/', CategoryView.as_view(), name='category-list'),  # 分类列表
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),  # 标签列表
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),  # 文章详情
    path('links/', LinkListView.as_view(), name='links'),  # 链接页面
    path('search/', SearchView.as_view(), name='search'),   # 搜索
    path('author/<int:owner_id>', AuthorView.as_view(), name='author'),  # 作者页面
    path('comment/', CommentView.as_view(), name='comment'),
    path('rss/', LatestPostFeed(), name='rss'),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
]
