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

