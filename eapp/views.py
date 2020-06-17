from django.shortcuts import render
# from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def index (request):
    return render(request, 'eapp/index.html')
