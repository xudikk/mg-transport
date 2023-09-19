from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from core.models import Department, User, UserDepartment, AutoMotoTransportModel, AutoMotoTransport
from core.forms import *


@login_required(login_url='login')
def gets(requests, key, pk=None, status=None):
    try:
        Model = {
            "departs": Department,
            'amodel': AutoMotoTransportModel,
            'transport': AutoMotoTransport,
        }[key]
        FormModel = {
            "departs": 'Department',
            "amodel": 'AutoModel',
            "transport": 'AutoMoto',
        }[key]
    except:
        return render(requests, 'base.html', {"error": 404})
    if status == "form":
        pagination = Model.objects.all().order_by('-pk')
        paginator = Paginator(pagination, settings.PAGINATE_BY)
        page_number = requests.GET.get("page", 1)
        paginated = paginator.get_page(page_number)

        ctx = {
            "roots": paginated,
            "pos": "list",
            key: "active"
        }

        root = Model.objects.filter(pk=pk).first()
        form = eval(f"{FormModel}Form")(requests.POST or None, requests.FILES or None, instance=root or None)
        if form.is_valid():
            form.save()
            return redirect('dashboard-auto-list', key=key)
        ctx["form"] = form
        ctx['suggest_status'] = "form"
        return render(requests, f'pages/{key}.html', ctx)
    elif pk:
        root = Model.objects.filter(pk=pk).first()
        ctx = {
            "pos": "one",
            'root': root,
            key: "active"
        }
        if not root:
            ctx['error'] = 404
    else:
        pagination = Model.objects.all().order_by('-pk')
        paginator = Paginator(pagination, settings.PAGINATE_BY)
        page_number = requests.GET.get("page", 1)
        paginated = paginator.get_page(page_number)

        ctx = {
            "roots": paginated,
            "pos": "list",
            key: "active"
        }

    return render(requests, f'pages/{key}.html', ctx)


@login_required(login_url='login')
def auto_form(requests, key, pk=None):
    try:
        Model = {
            "departs": Department,
            'amodel': AutoMotoTransportModel,
            'transport': AutoMotoTransport,
        }[key]
        FormModel = {
            "departs": 'Department',
            "amodel": 'AutoModel',
            "transport": 'AutoMoto',
        }[key]
    except:
        return render(requests, 'base.html', {"error": 404})
    root = None
    if pk:
        root = Model.objects.filter(pk=pk).first()
        if not root:
            ctx = {"error": 404}
            return render(requests, f'pages/{key}.html', ctx)

    form = eval(f"{FormModel}Form")(requests.POST or None, requests.FILES or None, instance=root)
    if form.is_valid():
        form.save()
        return redirect('dashboard-auto-list', key=key)

    ctx = {
        "form": form,
        "pos": 'form',
        key: "active"
    }
    return render(requests, f'pages/{key}.html', ctx)


@login_required(login_url='login')
def auto_del(requests, key, pk):
    try:
        Model = {
            "departs": Department,
            "amodel": AutoMotoTransportModel,
            'transport': AutoMotoTransport,
        }[key]
    except:
        return render(requests, 'base.html', {"error": 404})

    root = Model.objects.filter(pk=pk).first()
    if not root:
        ctx = {"error": 404}
        return render(requests, f'pages/{key}.html', ctx)
    root.delete()
    return redirect('dashboard-auto-list', key=key)
