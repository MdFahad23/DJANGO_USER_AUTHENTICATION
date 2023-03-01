from django.shortcuts import render

# Create your views here.
def index(request):
    diction = {}
    return render(request, 'Authentication/index.html', context=diction)
    
