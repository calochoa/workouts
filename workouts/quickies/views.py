import datetime
import random
from django.shortcuts import render
from .models import Quickie, Level, BodySplit, QuickieType

def home(request):
    today = datetime.date.today()
    quickies = Quickie.objects.all()
    index = today.toordinal() % quickies.count()
    quickie_of_the_day = quickies[index]
    return render(request, 'quickies/home.html', {'quickie': quickie_of_the_day})

def library(request):
    return render(request, 'quickies/library.html', __get_quickies_context(request))

def roulette(request):
    roulette_context = __get_quickies_context(request)
    quickies = roulette_context.pop('quickies', None)
    roulette_context['selected_quickie'] = random.choice(quickies) if quickies else None
    return render(request, 'quickies/roulette.html', roulette_context)

def __get_quickies_context(request):
    # Get filter params from GET request
    selected_level = request.GET.get("level")
    selected_body_split = request.GET.get("body_split")
    selected_type = request.GET.get("type")

    quickies = Quickie.objects.all()

    if selected_level:
        quickies = quickies.filter(q_level__l_name=selected_level)
    if selected_body_split:
        quickies = quickies.filter(q_body_split__bs_name=selected_body_split)
    if selected_type:
        quickies = quickies.filter(q_type__qt_name=selected_type)

    return {
        'quickies': quickies,
        'levels': Level.objects.all(),
        'body_splits': BodySplit.objects.all(),
        'types': QuickieType.objects.all(),
        'selected_type': selected_type,
        'selected_level': selected_level,
        'selected_body_split': selected_body_split,
        'total_results': quickies.count()
    }
