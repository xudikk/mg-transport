#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan

from django.urls import path, include

from core.dashboard.acrud import gets, auto_form, auto_del
from core.dashboard.auto import marka, color
from core.dashboard.view import index
from core.dashboard.auth import sign_in, sign_out, create_user

urlpatterns = [

    path("", index, name='home'),

    # auth
    path("login/", sign_in, name='login'),
    path('logout/', sign_out, name='log-out'),

    # auto
    path("auto/<key>/", gets, name="dashboard-auto-list"),
    path("auto/<key>/<int:pk>/", gets, name="dashboard-auto-detail"),
    path("auto/<key>/add/", auto_form, name="dashboard-auto-add"),
    path("auto/<key>/edit/<int:pk>/", auto_form, name="dashboard-auto-edit"),
    path("auto/<key>/del/<int:pk>/", auto_del, name="dashboard-auto-delete"),

    path('auto/<key>/form/<status>/', gets, name='dashboard-auto-ontime-add'),
    path('auto/<key>/form/<status>/<pk>/', gets, name='dashboard-auto-ontime-edit'),

    # dpartment auto
    path('department/<key>/<int:dpt_id>/', gets, name='department-auto-filtered'),
    # path('auto/<key>/form/add/<status>/<int:dpt_id>/', gets, name='dashboard-auto-ontime-add-by-user'),
    # path('auto/<key>/form/edit/<status>/<int:dpt_id>/<int:pk>/', gets, name='dashboard-auto-ontime-edit-by-user'),

    # marks
    path("marks/", marka, name="marks"),
    path("marks/<status>/", marka, name="marks_add"),
    path("marks/<status>/<int:pk>/", marka, name="marks_edit"),

    # marks
    path("color/", color, name="color"),
    path("color/<status>/", color, name="color_add"),
    path("color/<status>/<int:pk>/", color, name="color_edit"),

    # marks
    path("user/", create_user, name="user"),
    path("user/<status>/", create_user, name="user_add"),
    path("user/<status>/<int:pk>/", create_user, name="user_edit"),

]


