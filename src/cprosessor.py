#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.conf import settings
from django.core.handlers.wsgi import WSGIRequest


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
