from django.shortcuts import render

from .forms import MainForm


def index(request):
    context = {
        'form': MainForm(),
    }
    return render(request, 'mesite/index.html', context)
