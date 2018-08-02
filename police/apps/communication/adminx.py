import xadmin


from .models import Communication, StudyGarden


class CommunicationAdmin(object):
    #后台显示列表
    list_display = ['title', 'source', 'read_volume', 'add_time']
    #搜索
    search_fields = ['title', 'source']
    #筛选
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    #只读
    readonly_fields = ['read_volume']

    exclude = ['is_imgText']


class StudyGardenAdmin(object):
    # 后台显示列表
    list_display = ['title', 'source', 'read_volume', 'add_time']
    # 搜索
    search_fields = ['title', 'source']
    # 筛选
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    # 只读
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


xadmin.site.register(Communication, CommunicationAdmin)
xadmin.site.register(StudyGarden, StudyGardenAdmin)