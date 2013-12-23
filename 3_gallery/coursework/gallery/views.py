# -*- coding: utf-8 -*-
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import *
from gallery.models import *

class ImageList(ListView):
    template_name = 'gallery.html'
    model = Image

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("".join(x for x in request.FILES['image'].name if x.isalnum()))
            image = Image(image=request.FILES['image'],title=request.POST['title'],dsc=request.POST['dsc'])

            if request.FILES['image'].name.split('.')[-1] in {'jpg', 'jpeg', 'gif', 'png', 'bmp'}:
                image.save()
                return redirect("/gallery/")
            else:
                messages.error(request, (u'Wrong file format! Load: jpg, jpeg, gif, png, bmp'))
            return redirect("/")
        else:
            messages.error(request, (u'WRONG Form'))
    else:
        return render(request, "index.html")
