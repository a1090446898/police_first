import xadmin


from .models import Source, Notice, Announcement, WorkBulletin, Laws, TeamSystem, SpecialWork


class SourceAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class NoticeAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']


class AnnouncementAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']


class WorkBulletinAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']


class LawsAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']


class TeamSystemAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']


class SpecialWorkAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'data', 'add_time']
    search_fields = ['title', 'data']
    list_filter = ['title', 'data', 'add_time']


xadmin.site.register(Source, SourceAdmin)
xadmin.site.register(Notice, NoticeAdmin)
xadmin.site.register(Announcement, AnnouncementAdmin)
xadmin.site.register(WorkBulletin, WorkBulletinAdmin)
xadmin.site.register(Laws, LawsAdmin)
xadmin.site.register(TeamSystem, TeamSystemAdmin)
xadmin.site.register(SpecialWork, SpecialWorkAdmin)


