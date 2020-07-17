from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #the following line is redundant now because the render method automatically loads the template located
    #at in the templates directory structure of this app.
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

# Leave the rest of the views (detail, results, vote) unchanged