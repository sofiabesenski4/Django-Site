from django.shortcuts import render
from .models import Target
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


def index(request):
    targets_list = Target.objects.all()
    #the following line is redundant now because the render method automatically loads the template located
    #at in the templates directory structure of this app.

    context = {
        'targets': targets_list,
    }
    return render(request, 'word_count/index.html', context)

def details(request, target_id):
    target = get_object_or_404(Target, pk=target_id)
    context = {"target_id" : target_id,
               "body_text": target.body_set.all()[0],
               "target_text": target.target_text

               }
    return render(request, 'word_count/details.html', context)