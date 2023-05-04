from django.http import HttpResponse
from .models import Message


# Create your views here.

def homePageView(request):
    

    content = 'Hello Web!';
    print(request.GET['id'])
    mo = Message.objects.get(id=request.GET.get("id")) 
    content = mo.content
		
    return HttpResponse(content)
