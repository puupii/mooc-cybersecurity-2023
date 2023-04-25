from django.http import HttpResponse


# Create your views here.

def homePageView(request):
    return HttpResponse('Hello Web!')

def addView(request):
    firstnumber = int(request.GET.get('first'))
    secondnumber = int(request.GET.get('second'))
    result = firstnumber + secondnumber
    return HttpResponse(result)


def multiplyView(request):
    firstnumber = int(request.GET.get('first'))
    secondnumber = int(request.GET.get('second'))
    result = firstnumber * secondnumber
    return HttpResponse(result)
