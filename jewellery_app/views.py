from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import Slider, Subcategory, Category
from django.utils import timezone

# Create your views here.

def index(request):
    # sliders = get_object_or_404(Slider)
    # sliders = Slider.objects.all()
    # sliders = get_object_or_404(Slider)
    sliders = Slider.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    categories = Category.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'sliders': sliders, 'categories': categories})
    # return render(request, 'index.html')
    # return HttpResponse("this is homepage")