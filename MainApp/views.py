from django.shortcuts import render, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def home(request):
    return render(request, 'index.html')


def item_page(request, id):
    try:
        return render(request, 'item.html', {'item': Item.objects.get(pk=id)})
    except ObjectDoesNotExist:
        raise Http404(f'Товар с id={id} не найден')


def items_list(request):
    return render(request, 'items.html', {'items': Item.objects.all()})
