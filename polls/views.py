import time
import random
from django import forms

from django.http.response import HttpResponse
from django.shortcuts import render

from polls.helpers import calculate_sum
from polls.models import Question
from datetime import datetime

def index_view(request):
    user_agent = request.META['HTTP_USER_AGENT']

    return HttpResponse('Your user agent is: {}'.format(user_agent))


def contact_us_view(request):
    welcome_text = 'You opened page'
    result = None
    circles = []

    if request.method == 'POST':
        welcome_text = 'You have submitted form'
        number_a = int(request.POST['number_a'])
        number_b = int(request.POST['number_b'])

        result = calculate_sum(number_a, number_b)

        random_color = lambda: random.randint(0, 255)

        for n in range(result):
            color = 'rgb({r}, {g}, {b})'.format(
                r=random_color(),
                g=random_color(),
                b=random_color()
            )
            circles.append({
                'name': '#%s' % n,
                'color': color
            })

    context = {
        'current_time': time.strftime('%H:%M:%S %A'),
        'welcome_text': welcome_text,
        'result': result,
        'circles': circles
    }

    return render(request, 'contact_us.html', context=context)


def questions(request):
    from polls.models import Question
    from datetime import datetime

    # q = Question(question_text='How do you feel today?', pub_date=datetime.utcnow())
    # q.save()
    #
    # questions = Question.objects.all()

    if request.method == 'POST':
        question_text = request.POST['question_text']
        q = Question(question_text=question_text, pub_date=datetime.utcnow())
        q.save()

    all_questions = Question.objects.all()

    return render(request, 'question.html', context={'questions': all_questions})


def enter_question(request):

    if request.method == 'POST':
        question_text = request.POST['question_text']
        q = Question(question_text=question_text, pub_date=datetime.utcnow())
        q.save()
    all_questions = Question.objects.all()
    return render(request, 'question.html', context={'questions': all_questions})


from polls.models import Choice, Question
# all_questions = Question.objects.all()

def question_page(request, question_pk):
    question = Question.objects.get(pk=question_pk)

    if request.method == 'POST':
        answer = request.POST['answer']
        choice = Choice(question=question, choice_text=answer)
        choice.save()

    return render(request, 'question_detail.html', context={'question': question})
