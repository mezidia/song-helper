from django.shortcuts import render
from datetime import date
from .forms import InputForm


def index(request):
    result = ''
    year = date.today().year
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = text.capitalize()
    context = {
        'result': result,
        'form': InputForm(),
        'year': year,
    }
    return render(request, 'mesite/index.html', context)
