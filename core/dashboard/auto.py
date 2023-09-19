from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from core.forms.auto import AutoBrandForm, AutoColorForm
from core.models import AutoBrand, AutoMotoTransportColor


def marka(request, status=None, pk=None):
    pagination = AutoBrand.objects.all().order_by('-pk')
    paginator = Paginator(pagination, settings.PAGINATE_BY)
    page_number = request.GET.get("page", 1)
    paginated = paginator.get_page(page_number)
    ctx = {
        "roots": paginated,
        "pos": "list",
        'mar_active': "active",
    }
    if status == 'form':
        root = AutoBrand.objects.filter(pk=pk).first()
        form = AutoBrandForm(request.POST or None, instance=root or None)
        if form.is_valid():
            form.save()
            return redirect('marks')
        ctx["form"] = form
        ctx['suggest_status'] = "form"

    return render(request, f'pages/marka.html', ctx)


def color(request, status=None, pk=None):
    pagination = AutoMotoTransportColor.objects.all().order_by('-pk')
    paginator = Paginator(pagination, settings.PAGINATE_BY)
    page_number = request.GET.get("page", 1)
    paginated = paginator.get_page(page_number)
    ctx = {
        "roots": paginated,
        "pos": "list",
        'color_model': "active",
    }
    if status == 'form':
        root = AutoMotoTransportColor.objects.filter(pk=pk).first()
        form = AutoColorForm(request.POST or None, instance=root or None)
        if form.is_valid():
            form.save()
            return redirect('color')
        ctx["form"] = form
        ctx['suggest_status'] = "form"

    return render(request, f'pages/color.html', ctx)
