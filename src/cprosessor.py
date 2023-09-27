#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from contextlib import closing

from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest
from django.db import connection
from methodism import dictfetchall, dictfetchone


def main(requests):
    return {
        "app_name": settings.APP_NAME
    }


def ut(request):
    if request.user.is_anonymous:
        return {}
    if request.user.ut == 1:
        return {
            "ut_html": ['partials/superuser.html'],
            "user_sidebar": 'partials/susidebar.html'
        }
    else:
        return {
            "ut_html": ['partials/user.html'],
            "user_sidebar": 'partials/user_sidebar.html'
        }


def check_notifications(request):
    sql = """
        select moto.state_number, dpt.name as depart, use.name as user, notes.last_change, notes.change_type  from auto_moto_transport moto
        left join core_notificationmodel notes on notes.transport_id = moto.id
        left join core_user use on use.id = notes.user_id
        left join department dpt on dpt.id = use.depart_id 
        where not moto.status == 'active'
        group by moto.id
        limit 3
    """
    cnt = """
        select count(*) as cnt  from auto_moto_transport moto
        where not moto.status == 'active'
        limit 1
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        notes = dictfetchall(cursor)

        cursor.execute(cnt)
        cnt = dictfetchone(cursor)

    return {
        "notes": notes,
        "cnt": cnt
    }

