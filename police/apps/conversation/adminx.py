import xadmin


from .models import Communication, StudyGarden


class CommunicationAdmin(object):
    #后台显示列表
    list_display = ['title', 'read_volume', 'add_time']
    #搜索
    search_fields = ['title']
    #筛选
    list_filter = ['title', 'read_volume', 'add_time']
    #只读
    readonly_fields = ['read_volume']

    style_fields = {'content': 'ueditor'}


class StudyGardenAdmin(object):
    # 后台显示列表
    list_display = ['title', 'read_volume', 'add_time']
    # 搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['title', 'read_volume', 'add_time']
    # 只读
    readonly_fields = ['read_volume']
    style_fields = {'content': 'ueditor'}


xadmin.site.register(Communication, CommunicationAdmin)
xadmin.site.register(StudyGarden, StudyGardenAdmin)
