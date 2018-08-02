import xadmin


from .models import Source, Notice, Announcement, WorkBulletin, Laws, TeamSystem, SpecialWork


class SourceAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class NoticeAdmin(object):
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class AnnouncementAdmin(object):
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class WorkBulletinAdmin(object):
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class LawsAdmin(object):
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class TeamSystemAdmin(object):
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class SpecialWorkAdmin(object):
    list_display = ['title', 'data', 'add_time']
    search_fields = ['title', 'data']
    list_filter = ['title', 'data', 'add_time']
    exclude = ['is_imgText']


xadmin.site.register(Source, SourceAdmin)
xadmin.site.register(Notice, NoticeAdmin)
xadmin.site.register(Announcement, AnnouncementAdmin)
xadmin.site.register(WorkBulletin, WorkBulletinAdmin)
xadmin.site.register(Laws, LawsAdmin)
xadmin.site.register(TeamSystem, TeamSystemAdmin)
xadmin.site.register(SpecialWork, SpecialWorkAdmin)


