from django import forms


class Content(forms.Form):
    content = forms.CharField(label = "new note", max_length=100)
