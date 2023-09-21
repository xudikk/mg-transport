#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.conf import settings


def main(requests):
    return {
        "app_name": settings.APP_NAME
    }


def ut(request):
    if request.user.is_anonymous:
        return {}
    utypes = {
        1: ['partials/superuser.html'],
        2: ['partials/user.html']
    }.get(request.user.ut, ['partials/user.html'])

    return {
        "ut_html": utypes
    }

