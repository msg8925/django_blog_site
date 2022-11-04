from django.shortcuts import render

# function-based views here.
def home(request):

    

    return render(request, 'blog/home.html')