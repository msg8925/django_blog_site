from django.shortcuts import render
from users.forms import UserRegistrationForm

# Create your views here.

def register(request):

    # If the user submits a form
    if request.method == 'POST':
        form = UserRegistrationForm(request.form)


    form = UserRegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'users/register.html', context)

