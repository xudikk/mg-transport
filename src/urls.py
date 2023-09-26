#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings

from django.views.static import serve


def page_not_found_view(request, exception):
    return render(request, 'pages/abs404.html', context={"error": 404}, status=404)


def error_500(request, exception):
    return render(request, 'pages/abs500.html', context={}, status=500)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("core.urls"))
]

urlpatterns += [

    path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]

handler404 = "src.urls.page_not_found_view"
handler500 = "src.urls.error_500"
