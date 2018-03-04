from django.shortcuts import get_object_or_404, render  #1 shortcut
from django.http import HttpResponse #2 기본적인 출력을 위한 도구
from django.template import loader #3 template loader  //shortcut을 사용하면 import할 필요가 없다.
from django.http import Http404

from .models import Question


def index(request):
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)""" # hard coding

    """latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    """ # 정석적인 방법

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)       #1 short cut을 이용한 index() view

def detail(request, question_id):
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html', {'question': question})
    """ # 기존 예외처리 방식
    
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
