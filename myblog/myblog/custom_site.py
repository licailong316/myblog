from django.contrib.admin.sites import AdminSite


class CustomSite(AdminSite):
    site_header = 'MyBlog'
    site_title = 'MyBlog管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
