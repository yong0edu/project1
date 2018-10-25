
from django.shortcuts import render, redirect
from lotto.forms import PostForm
from .models import *

def index(request):
    lottos = GuessNumbers.objects.all()
    location = Location.objects.get(id=1)
    return render(
        request,
        'lotto/index.html',
        {
            'lottos':lottos, 'location':location
         }
    )


def post(request):
     if request.method == 'GET':
        form = PostForm()
        return render(request, 'lotto/form.html', {'form': form})
     else:
         form = PostForm(request.POST)
         if form.is_valid():
             lotto = form.save(commit=False)
             lotto.generate()
             return redirect('/lotto')





