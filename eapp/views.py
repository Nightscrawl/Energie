from django.shortcuts import render
from .models import *
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.


def index (request):
    return render(request, 'eapp/index.html')

def getExerciseTypes(request):
    type_list=ExerciseType.objects.all()
    return render(request, 'eapp/extypes.html', {'type_list': type_list})

def getExercises(request):
    exercise_list=Exercise.objects.all()
    return render(request, 'eapp/exercises.html', {'exercise_list': exercise_list})

def exerciseDetails(request, id):
    exer=get_object_or_404(Exercise, pk=id)  # don't forget the model name here!!
    context={
        'exer' : exer,
    }
    return render(request, 'eapp/exdetails.html', context=context)
