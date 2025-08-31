from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

# كاش 15 دقيقة (900 ثانية)
@cache_page(60 * 15)
def property_list(request):
    properties = Property.objects.all().values("id", "title", "description", "price", "location")
    return JsonResponse(list(properties), safe=False)
