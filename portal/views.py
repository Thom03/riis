from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize

from .models import *

# Create your views here.

class Portal(TemplateView):
	template_name = "portal.html"
    
def houses_view(request):
    house_as_geojson = serialize('geojson', Houses.objects.all())
    return HttpResponse(house_as_geojson , content_type='json')

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(name_icontains=query)


def roads_view(request):
    road_as_geojson = serialize('geojson', Road.objects.all())
    return HttpResponse(road_as_geojson , content_type='json')	

def boundary_view(request):
    boundary_as_geojson = serialize('geojson', boundary.objects.all())
    return HttpResponse(boundary_as_geojson , content_type='json')

def highway_view(request):
    highway_as_geojson = serialize('geojson', Highway.objects.all())
    return HttpResponse(highway_as_geojson , content_type='json')

def procareas_view(request):
    procted_as_geojson = serialize('geojson', procareas.objects.all())
    return HttpResponse(procted_as_geojson , content_type='json')    	    	           	    