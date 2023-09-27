from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from base.helper import perm_helper
from core.models import Department, User, AutoMotoTransportModel, AutoMotoTransport
from core.forms import *


@perm_helper
def transport_gets(requests, pk=None, status=None, dpt_id=None):
    if status == "form":
        if requests.user.ut != 1:
            pagination = AutoMotoTransport.objects.filter(department_id=requests.user.depart.id)
        else:
            pagination = AutoMotoTransport.objects.all()
        paginator = Paginator(pagination, settings.PAGINATE_BY)
        page_number = requests.GET.get("page", 1)
        paginated = paginator.get_page(page_number)

        ctx = {
            "roots": paginated,
            "pos": "list",
            'transport': "active"
        }

        root = AutoMotoTransport.objects.filter(pk=pk, status='active').first()
        kwar = {
            'instance': root or None,
            'department': requests.user.depart or None
        }
        form = AutoMotoForm(requests.POST or None, requests.FILES or None, **kwar)
        if form.is_valid():
            if kwar.get('instance'):
                change_type = "edit"
            else:
                change_type = "add"
            form.save(user=requests.user, change_type=change_type)

            if dpt_id:
                return redirect('transport-auto-filtered', dpt_id=requests.user.depart.id)
            else:
                return redirect('transport-list')
        ctx["form"] = form
        ctx['suggest_status'] = "form"
        return render(requests, f'pages/transport.html', ctx)
    elif pk:
        root = AutoMotoTransport.objects.filter(pk=pk, status='active').first()
        ctx = {
            "pos": "one",
            'root': root,
            'transport': "active"
        }
        if not root:
            ctx['error'] = 404
    else:

        if dpt_id:
            pagination = AutoMotoTransport.objects.filter(department_id=dpt_id)
        else:
            pagination = AutoMotoTransport.objects.all()

        paginator = Paginator(pagination, settings.PAGINATE_BY)
        page_number = requests.GET.get("page", 1)
        paginated = paginator.get_page(page_number)

        ctx = {
            "roots": paginated,
            "pos": "list",
            'transport': "active"
        }

    return render(requests, f'pages/transport.html', ctx)


@perm_helper
def notifications(request):
    pagination = AutoMotoTransport.objects.filter(status='waiting')
    paginator = Paginator(pagination, settings.PAGINATE_BY)
    page_number = request.GET.get("page", 1)
    paginated = paginator.get_page(page_number)

    ctx = {
        "roots": paginated,
        "pos": "list",
        'transport': "active",
        'next': 'notes'
    }

    return render(request, f'pages/transport.html', ctx)


@perm_helper
def conf_or_delete(request, status, pk):
    root = AutoMotoTransport.objects.filter(pk=pk).first()
    try:
        if status == 'conf':
            root.status = 'active'
            root.change = False
            root.save()
        elif status == 'delete':
            root.delete()
    except:
        pass
    redirect_path = request.GET.get('next')
    return redirect(redirect_path or 'transport-list')
