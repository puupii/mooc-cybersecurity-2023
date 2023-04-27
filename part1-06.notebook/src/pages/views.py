from django.shortcuts import render
from .forms import Content

# Create your views here.


def addPageView(request):
    if request.method == "POST":
        form = Content(request.POST)
        print(form)
        if form.is_valid():
            print(form.cleaned_data)
            new_note = form.cleaned_data['content']
            items = request.session.get('items', [])
            if len(items) > 9:
                items.pop(0)
            items.append(new_note)
            request.session['items'] = items

    print(items)
    return render(request, 'pages/index.html', {'items': items})


def erasePageView(request):
    if request.method == "POST":
        items = request.session.get('items')
        items = []
        request.session['items'] = items

        content = request.session.get('content')
        content = ''
        request.session['content'] = content

    return render(request, 'pages/index.html', {'items' : items})


def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
