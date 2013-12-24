# -*- coding: utf-8 -*-
from django.forms import ModelForm
from gallery.models import *


class ImageForm(ModelForm):
    class Meta:
        model = Image
