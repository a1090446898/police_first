import xadmin


from .models import DutyMan


class DutyManAdmin(object):
    list_display = ['time', 'leader', 'leader_phone', 'follower', 'telephone', 'follower_phone',
                    'add_time']

    search_fields = ['time', 'leader', 'leader_phone', 'follower', 'telephone', 'follower_phone']

    list_filter = ['time', 'leader', 'leader_phone', 'follower', 'telephone', 'follower_phone',
                   'add_time']


xadmin.site.register(DutyMan, DutyManAdmin)
