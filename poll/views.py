from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# Create your views here.
''' def index(request):
    try:
        recent_questions = Question.objects.order_by('pub_date')[:5]
        context = {'recent_questions': recent_questions}
    except IndexError:
        return Http404 
    return render(request, 'poll/index.html', context)'''

class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'recent_questions'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]


''' def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}

    return render(request, 'poll/detail.html', context) '''

class DetailView(generic.DetailView):
    model=Question
    template_name = 'poll/detail.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError or Choice.DoesNotExist):
        return render(request, 'poll/detail.html', {'question': question, 'error_message': "You didn't select a choice"})

    else:
        selected_choice.choice_vote+=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

''' def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question} 
    return render(request, 'poll/results.html', context)'''

class ResultView(generic.DetailView):
    model=Question
    template_name = 'poll/results.html'

    
    
    