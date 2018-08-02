import xadmin


from .models import Duty, DutyMan


class DutyAdmin(object):
    list_display = ['week', 'add_time']
    search_fields = ['week']
    list_filter = ['week', 'add_time']


class DutyManAdmin(object):
    list_display = ['time', 'type', 'name', 'telephone', 'phone', 'add_time']
    search_fields = ['time', 'type', 'name', 'telephone', 'phone']
    list_filter = ['time__week', 'type', 'name', 'telephone', 'phone', 'add_time']


xadmin.site.register(Duty, DutyAdmin)
xadmin.site.register(DutyMan, DutyManAdmin)