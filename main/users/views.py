from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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


@login_required
def profile(request):

    if request.method == 'POST':
        form_u = UserUpdateForm(request.POST, instance=request.user)
        form_p = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form_u.is_valid() & form_p.is_valid():
            form_u.save()
            form_p.save()
            messages.success(request, 'Profile Updated') 
            return redirect('profile')


    else:
        form_u = UserUpdateForm(instance=request.user)
        form_p = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'form_u': form_u,
        'form_p': form_p
    }

    return render(request, 'users/profile.html', context)