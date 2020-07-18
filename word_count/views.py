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
from .forms import WebScrapeForm
from django.utils import timezone

def index(request):
    target_list = Target.objects.all()
    #the following line is redundant now because the render method automatically loads the template located
    #at in the templates directory structure of this app.

    context = {
        'target_list': target_list,
    }
    return render(request, 'word_count/index.html', context)

def details(request, target_id):
    target = get_object_or_404(Target, pk=target_id)
    context = {"target_id" : target_id,
               "body_text": target.body_set.all()[0],
               "target_text": target.target_text

               }
    return render(request, 'word_count/details.html', context)

def search(request):
    if request.method== "POST":
        #we need to validate the form, so take the info from the HTTPRequest and populate a new WebScrapeForm with ti
        context={}
        form = WebScrapeForm(request.POST)
        if form.is_valid():
            target = Target.objects.create(search_date=timezone.now(), target_text=form.cleaned_data["search_url"])
            scraped_body = target.body_set.create(body_text=web_scrape(target.target_text))
            target.save()
            return HttpResponseRedirect(reverse("word_count:index"))
        context["error_message"]= "Form field invalid"
        return render(request, reverse('word_count:search'), context)
    else:
        #then this is the user's first intereaction with the form view: need to populate the form without
        #any values, and allow user to enter a URL
        context = {
            'form' : WebScrapeForm()}
        return render(request, 'word_count/search.html', context)

def web_scrape(url):
    return "TESTING SCRAPED WEB COfadfdssfNTENT"