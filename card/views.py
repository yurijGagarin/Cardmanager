import random
from datetime import datetime, timedelta

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.urls import reverse
from card.forms import GeneratorForm, CardEditForm
from card.models import Card, CardTransaction
from django.http import HttpResponseRedirect
from card.filters import CardFilter
import ccard


def list(request):
    card_list = Card.objects.all()
    filter = CardFilter(request.GET, queryset=card_list)
    card_list = filter.qs

    paginator = Paginator(card_list, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'filter': filter
    }
    return render(request, 'list.html', context)


class CardGenerator(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'generator.html', context={'form': GeneratorForm()})

    def post(self, request, *args, **kwargs):

        form = GeneratorForm(request.POST)
        if form.is_valid():
            for i in range(form.cleaned_data['amount_to_generate']):
                model = Card(
                    serial_number=form.cleaned_data['serial_number'],
                    card_number=ccard.visa(),
                    release_date=form.cleaned_data['released'],
                    exp_date=form.cleaned_data['released'] + timedelta(weeks=4 * form.cleaned_data['ttl']),
                    cvv=random.randrange(100, 1000),
                    balance=0,

                )
                model.save()
            return HttpResponseRedirect('/card/list')
        else:
            return render(request, 'generator.html', context={'form': form})


class CardInfo(View):
    def get(self, request, pk, *args, **kwargs):
        card = Card.objects.get(id=pk)
        card_transactions = card.cardtransaction_set.all()

        form = CardEditForm({"card_status": card.card_status})

        paginator = Paginator(card_transactions, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'card': card,
            'card_transactions': card_transactions,
            'form': form,
        }

        return render(request, 'info.html', context)

    def post(self, request, pk, *args, **kwargs):
        card = Card.objects.get(id=pk)

        form = CardEditForm(request.POST)
        if form.is_valid():
            card.card_status = form.cleaned_data['card_status']
            card.save()
            return HttpResponseRedirect('/card/list')
        else:
            return render(request, 'info.html', context={'form': form})


def delete(request, pk):
    card = Card.objects.get(id=pk)
    card.delete()
    return HttpResponseRedirect(reverse('/cardlist'))
