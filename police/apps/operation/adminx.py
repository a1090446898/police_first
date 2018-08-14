import xadmin


from .models import Submission, SubmissionPass, SubmissionRead


from xadmin import views


# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True


class GlobalSettings(object):
    site_title = '遵义市公安局'
    site_footer = '遵义市公安局'
    # menu_style = 'accordion'  # 收起导航栏


class SubmissionAdmin(object):
    list_display = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time']
    search_fields = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email']
    list_filter = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time']
    # readonly_fields = ['title', 'name', 'phone', 'address', 'email', 'add_time', 'content']

    def queryset(self):
        qs = super(SubmissionAdmin, self).queryset()
        qs = qs.filter(is_pass=False, is_read=False)
        return qs


class SubmissionPassAdmin(object):
    list_display = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time']
    search_fields = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email']
    list_filter = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time']
    # readonly_fields = ['title', 'name', 'phone', 'address', 'email', 'add_time', 'content']

    def queryset(self):
        qs = super(SubmissionPassAdmin, self).queryset()
        qs = qs.filter(is_pass=True)
        return qs


class SubmissionReadAdmin(object):
    list_display = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time', 'read_volume']
    search_fields = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'read_volume']
    list_filter = ['title', 'name', 'is_read', 'is_pass', 'phone', 'address', 'email', 'add_time', 'read_volume']

    readonly_fields = ['title', 'name', 'phone', 'address', 'email', 'add_time', 'content', 'read_volume']

    def queryset(self):
        qs = super(SubmissionReadAdmin, self).queryset()
        qs = qs.filter(is_pass=False, is_read=True)
        return qs


xadmin.site.register(SubmissionRead, SubmissionReadAdmin)
xadmin.site.register(SubmissionPass, SubmissionPassAdmin)
xadmin.site.register(Submission, SubmissionAdmin)


# 后台设置
# xadmin.site.register(views.BaseAdminView, BaseSetting)
# 主题功能
xadmin.site.register(views.CommAdminView, GlobalSettings)