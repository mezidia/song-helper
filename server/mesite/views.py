from django.shortcuts import render
from .forms import InputForm


def index(request):
    result = ''
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = text.capitalize()
    context = {
        'result': result,
        'form': InputForm(),
    }
    return render(request, 'mesite/index.html', context)
