from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def unit_content(request):
    return HttpResponse("This would be the unit page")