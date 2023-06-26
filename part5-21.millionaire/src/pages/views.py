from django.shortcuts import render, redirect
from .models import questions
import json

def find_topic(tid):
    for q in questions:
        if q['id'] == tid:
            return q
    return None


def quizView(request, tid):
    topic = find_topic(tid)

    request.session['level'] = 0
    return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][0]})


def answerView(request, tid, aid):
    topic = find_topic(tid)
    value = request.COOKIES.get('topic')
    print(type(topic),type(value))
    if value != topic['name']:
        return redirect('/cheater/')
    else:
        level = request.session['level']

    if topic['questions'][level]['correct'] == aid:
        level += 1
        request.session['level'] = level

        if level == len(topic['questions']):
            response = redirect('/finish/')
            response.set_cookie(key='winner', value='true')
            return response

        return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][level]})
    else:
        return redirect('/incorrect/')


def incorrectView(request):
    response = render(request, 'pages/incorrect.html')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response
    #return render(request, 'pages/incorrect.html')


def finishView(request):
    print(request.COOKIES)
    if request.COOKIES.get('winner') == 'true':
        return render(request, 'pages/finish.html')
    else:
        return redirect('/cheater/')


def cheaterView(request):
    response = render(request, 'pages/cheater.html')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response
#return render(request, 'pages/cheater.html')


def thanksView(request):
    response = render(request, 'pages/thanks.html')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    # Like we were going to pay anyone
    return response
#return render(request, 'pages/thanks.html')


def topicView(request, tid):
    value = request.COOKIES.get('topic')
    topic = find_topic(tid)
    if value is None:
        response = render(request, 'pages/topic.html', {'topic' : topic})
        response.set_cookie(key='topic', value=topic['name'])
    elif value != topic['name']:
        response = redirect('/cheater/')
    return response


def topicsView(request):
    value = request.COOKIES.get('topic')
    if value is None:
        response = render(request, 'pages/topics.html', {'questions' : questions})
    else:
        response = redirect('/cheater/')
    return response
#return render(request, 'pages/topics.html', {'questions' : questions})


