from django.shortcuts import render
from .forms import MainForm


def index(request):
    result = ''
    if request.method == 'POST':
        form = MainForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = text.capitalize()
    context = {
        'result': result,
        'form': MainForm(),
    }
    return render(request, 'mesite/index.html', context)
