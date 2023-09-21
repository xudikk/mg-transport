#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from base.helper import cnts


@login_required(login_url='login')
def index(request):
    ctx = {}
    if request.user.ut == 1:
        ctx = {
            'active': "active",
            'cnts': cnts(),
        }
    return render(request, 'pages/index.html', ctx)
