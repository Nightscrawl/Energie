from django.shortcuts import render
from .models import *
# from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.


def index (request):
    return render(request, 'eapp/index.html')

def getExerciseTypes(request):
    type_list=ExerciseType.objects.all()
    return render(request, 'eapp/extypes.html', {'type_list': type_list})
