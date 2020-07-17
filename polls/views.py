from django.shortcuts import render

# Create your views here.
from .models import Question
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic



#these views are using a generic template provided by the django framework
#this is a common control pattern in these applications so it is streamlining this process:
#   1) get data from database based on some parameter passed via the url
#   2) loading a template with the dat
#   3) return the template to the browser


#this generic view is meant to display a list of objects
class IndexView(generic.ListView):
    #template_name is used a variable used to tell django which template to use
    template_name = 'polls/index.html'
    #context_object_name will provide the view with the name of the list we are showing to the browser
    #auto generated name is possible, but ould be question_list, and we are only looking at 5 most
    #recent, so it is relevant to define this explicitly
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

#display a detailed page for a particular object
#expects the primary key value captured from the URL to be called "pk"
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



#this view is still hardcoded since this modifies data, and has some backend logic which isnt
#represented in the built-in generic views
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


