from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.contrib import messages

# Create your views here.

def register(request):

    # If the user submits a form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. Log in now.')
            return redirect('blog-home')


    form = UserRegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)

