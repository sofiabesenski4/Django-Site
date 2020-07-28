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
    return render(request, "word_count/index.html", context)

def details(request, target_id):
    target = get_object_or_404(Target, pk=target_id)
    context = {"target_id" : target_id,
               "body_text": target.body_text,
               "target_text": target.target_text

               }
    return render(request, 'word_count/details.html', context)
def analyze(request, target_id):
    context= {}
    return render(request, reverse('word_count:analyze').strip('/')+ ".html", context)

def search(request):
    if request.method== "POST":
        #we need to validate the form, so take the info from the HTTPRequest and populate a new WebScrapeForm with ti
        context={}
        form = WebScrapeForm(request.POST)
        if form.is_valid():
            try:

                scraped_data = web_scrape(form.cleaned_data["search_url"])
                if scraped_data:
                    this_target = Target.objects.create(search_date=timezone.now(), target_text=form.cleaned_data["search_url"], body_text =scraped_data[:20000] )
                    this_target.wordList_set.create({"a":1})
                    return HttpResponseRedirect(reverse("word_count:index"))
                else:
                    raise Exception
            except:
                context["error_message"]= "exception after form was validated"
                context["form"]= form

                return render(request, reverse('word_count:search').strip('/')+".html", context)
        else:
            context["error_message"] = "URL or Web Error"
            context["form"] = form

            return render(request, reverse('word_count:search').strip('/')+".html", context)

    else:
        #then this is the user's first intereaction with the form view: need to populate the form without
        #any values, and allow user to enter a URL
        context = {
            'form' : WebScrapeForm()}

        return render(request, reverse('word_count:search').strip('/')+".html", context)


#NOTE: Normally this code should be kept in a location that ISNT the public django server, for security/exploit reasons
import urllib.request
import re
from bs4 import BeautifulSoup
from urllib.error import HTTPError

def web_scrape(url):
    try:
        response = urllib.request.urlopen(url)
    except HTTPError as e:
        print(e)
        raise Exception("HTTPError")
    soup = BeautifulSoup(response, 'html.parser')

    return soup.get_text()

def find_most_common_words(text):
    return {"f":0}
