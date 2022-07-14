import random
from datetime import datetime, timedelta

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View

from card.forms import GeneratorForm
from card.models import Card
from django.http import HttpResponseRedirect
from card.filters import CardFilter
import ccard

def list(request):
    contact_list = Card.objects.all()
    paginator = Paginator(contact_list, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    myFilter = CardFilter()
    context ={
        'page_obj': page_obj,
        'myFilter': myFilter
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
                    end_date=datetime.now() + timedelta(weeks=4*form.cleaned_data['ttl']),
                    cvv=random.randrange(100, 1000),
                    money_on_card=0,

                )
                model.save()
            return HttpResponseRedirect('/card/list')
        else:
            return render(request, 'generator.html', context={'form': form})

def account(request, pk):
    card = Card.objects.get(id=pk)
    context ={
        'card': card
    }
    return render(request, 'account.html', context)