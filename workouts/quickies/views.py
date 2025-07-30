import datetime
import random
from django.shortcuts import render
from django.http import Http404
from django.db.models.functions import Lower
from .models import Quickie, Level, BodySplit, QuickieType, Exercise

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

    quickies = Quickie.objects.all().order_by('q_type__id', 'q_level__l_value', 'q_name')

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

def exercises(request):
    # Get filter params from GET request
    selected_level = request.GET.get("level")
    selected_body_split = request.GET.get("body_split")

    exercises = Exercise.objects.all().order_by(Lower('e_name'))

    if selected_level:
        exercises = exercises.filter(e_level__l_name=selected_level)
    if selected_body_split:
        exercises = exercises.filter(e_body_split__bs_name=selected_body_split)

    exercises_context = {
        'exercises': exercises,
        'levels': Level.objects.all(),
        'body_splits': BodySplit.objects.all(),
        'selected_level': selected_level,
        'selected_body_split': selected_body_split,
        'total_results': exercises.count()
    }
    return render(request, 'quickies/exercises.html', exercises_context)


def exercise_detail(request, exercise_id):
    if not exercise_id:
        raise Http404("Exercise ID not provided.")

    try:
        exercise = Exercise.objects.select_related('e_level', 'e_body_split').get(id=exercise_id)
    except Exercise.DoesNotExist:
        raise Http404("Exercise not found.")

    return render(request, 'quickies/exercise_detail.html', {'exercise': exercise})
