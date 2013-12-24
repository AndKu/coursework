# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import *
from gallery.forms import ImageForm
from gallery.models import *

class ImageList(ListView):
    template_name = 'gallery.html'
    context_object_name = 'images'
    model = Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image(image=request.FILES['image'],title=request.POST['title'],dsc=request.POST['dsc'])
            image.save()
            return HttpResponseRedirect("/gallery/")
        else:
            messages.error(request, (u'WRONG Form'))
    else:
        form = ImageForm()
        return render(request, "index.html", {
            'form': form,
        })
