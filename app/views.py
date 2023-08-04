import os
from django.shortcuts import render, redirect

from app.models import ImageModel

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def index(request):
    if request.method=="POST":
        img = request.FILES.get('watermark-file')
        ImageModel.objects.create(image=img)
        
        return redirect('/')
    context = {}
    return render(request, 'app/index.html', context)