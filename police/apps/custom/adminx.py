import xadmin

from .models import LogoImage, MovieWindow, OtherConnections


class LogoImageAdmin(object):
    list_display = ['title', 'image', 'add_time']
    search_fields = ['title', 'image']
    list_filter = ['title', 'image', 'add_time']


class MovieWindowAdmin(object):
    list_display = ['title', 'image', 'is_window', 'add_time']
    search_fields = ['title', 'is_window', 'image']
    list_filter = ['title', 'image', 'is_window', 'add_time']


class OtherConnectionsAdmin(object):
    list_display = ['title', 'url', 'add_time']
    search_fields = ['title', 'url']
    list_filter = ['title', 'url', 'add_time']


xadmin.site.register(LogoImage, LogoImageAdmin)
xadmin.site.register(MovieWindow, MovieWindowAdmin)
xadmin.site.register(OtherConnections, OtherConnectionsAdmin)
