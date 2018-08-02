import xadmin


from .models import Submission, Plate


from xadmin import views


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True


class GlobalSettings(object):
    site_title = '遵义市公安局'
    site_footer = '遵义市公安局'
    # menu_style = 'accordion'  # 收起导航栏


# class PlateAdmin(object):
#     list_display = ['name']
#     search_fields = ['name']
#     list_filter = ['name']
#

class SubmissionAdmin(object):
    list_display = ['plate', 'title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time']
    search_fields = ['plate', 'title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email']
    list_filter = ['plate', 'title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time']
    # readonly_fields = ['title', 'name', 'phone', 'address', 'email', 'add_time', 'content']
    exclude = ['is_imgText']


# xadmin.site.register(Plate, PlateAdmin)
xadmin.site.register(Submission, SubmissionAdmin)


# 后台设置
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# 主题功能
xadmin.site.register(views.CommAdminView, GlobalSettings)