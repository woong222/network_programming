from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Choice, Question
from django.views import generic
from django.views.generic import ListView, DetailView


# Create your views here.
'''
def index(requsest):
    lastest_question_list = Question.objects.all().order_by('-pub_data')[:5]
    context = {'latest_question_list': lastest_question_list}
    return render(requsest, 'polls/index.html', context)

def detail(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question':question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question': question})
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class VoteView(generic.DetailView):
    model = Question
    template_name = 'polls/vote.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
