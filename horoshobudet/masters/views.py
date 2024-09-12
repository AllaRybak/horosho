from django.http import HttpResponseNotFound
from django.views.generic import ListView

from masters.models import Photos, Contract
from masters.utils import menu, promo


# Create your views here.
class ContractList(ListView):
    """ Представление для отображения объектов по адресам"""
    model = Contract
    template_name = 'masters/index.html'
    context_object_name = 'contracts'

    extra_context = {
        'title': 'Всё будет хорошо',
        'menu': menu,
        'promo': promo,
    }


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
