import xadmin


from .models import Resources


class ResourcesAdmin(object):
    list_display = ['title', 'download', 'add_time']
    search_fields = ['title']
    list_filter = ['title', 'download', 'add_time']


xadmin.site.register(Resources, ResourcesAdmin)