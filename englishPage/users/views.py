from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForms
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-login-page')
    else:
        form = SignUpForms()

    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)
