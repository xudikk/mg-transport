#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
import datetime
from contextlib import closing

from django.conf import settings
from random import randint

from django.db import connection
from methodism import dictfetchone


def cnts():
    sql = """
        SELECT (SELECT COUNT(*)
        FROM department) AS dp,
        (SELECT COUNT(*)
        FROM   auto_moto_transport) AS amt,
        (SELECT COUNT(*)
        FROM   core_user) AS cu, 

        (SELECT COUNT(*) FROM  core_automototransportmodel) AS mods
        FROM core_user
        limit 1
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        res = dictfetchone(cursor)

    return res


def unique_card():
    number = "8800 " + " ".join([str(randint(1000, 9999)) for x in range(3)])
    with open("base/numbers.txt", "r") as file:
        if number not in file.read().replace('\n', '').split(","):
            file = open("base/numbers.txt", "a")
            file.write(number + ",\n")
            return number
        else:
            return unique_card()


def lang_helper(request):
    if not request.user.is_anonymous:
        return request.user.lang
    return settings.DEFAULT_LANG


def card_mask(number):
    return number[0:4] + ' **** ****' + number[14:]


def generate_number():
    return unique_card()
