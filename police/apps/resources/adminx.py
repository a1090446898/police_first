import xadmin


from .models import Resources


class ResourcesAdmin(object):
    list_display = ['name', 'download', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'download', 'add_time']


xadmin.site.register(Resources, ResourcesAdmin)