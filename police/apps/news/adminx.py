import xadmin


from .models import News, HelpNews, PlacesNews, TeamNews, BuildWork, VideoPatrol,BannerNews


class NewsAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'is_banner', 'add_time']
    search_fields = ['title', 'source', 'is_banner', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'is_banner', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']

    def queryset(self):
        qs = super(NewsAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerNewsAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'is_banner', 'add_time']
    search_fields = ['title', 'source', 'is_banner', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'is_banner', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']

    def queryset(self):
        qs = super(BannerNewsAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class HelpNewsAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class PlacesNewsAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class TeamNewsAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class BuildWorkAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


class VideoPatrolAdmin(object):
    style_fields = {'content': 'ueditor'}
    list_display = ['title', 'source', 'read_volume', 'add_time']
    search_fields = ['title', 'source', 'read_volume']
    list_filter = ['title', 'source', 'read_volume', 'add_time']
    readonly_fields = ['read_volume']
    exclude = ['is_imgText']


# class BannerAdmin(object):
#     list_display = ['title', 'image', 'url', 'index', 'add_time']
#     search_fields = ['title', 'image', 'url', 'index']
#     list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(BannerNews, BannerNewsAdmin)
xadmin.site.register(News, NewsAdmin)
xadmin.site.register(HelpNews, HelpNewsAdmin)
xadmin.site.register(PlacesNews, PlacesNewsAdmin)
xadmin.site.register(TeamNews, TeamNewsAdmin)
xadmin.site.register(BuildWork, BuildWorkAdmin)
xadmin.site.register(VideoPatrol, VideoPatrolAdmin)
