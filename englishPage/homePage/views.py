from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import PostModel
from .forms import PostModelForm
from .models import DictionaryModel




# Create your views here.

def index(request):
    return render(request, 'index.html')

def text(request):
    return render(request, 'text.html')

def profil(request):

    if str(request.user) == "AnonymousUser":
        posts = PostModel.objects.all()
    else:
        posts = PostModel.objects.filter(author=request.user)

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        context = {
            'posts': posts,
            'form': form
        }

        if posts:
            posts.delete()
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('profil-page')
        else:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('profil-page')
    else:
        form = PostModelForm()
        context = {
            'posts': posts,
            'form': form
        }
    return render(request, 'profil.html', context)

def dictionary(request):

    if str(request.user) == "AnonymousUser":
        posts = DictionaryModel.objects.all()
    else:
        posts = DictionaryModel.objects.filter(user=request.user)

    context = {
        'posts': posts
    }
    return render(request, 'dictionary.html', context)

