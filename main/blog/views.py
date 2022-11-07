from django.shortcuts import render
from .models import Post 
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# function-based views here.
def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


#def post(request):

#    return render(request, 'blog/post-create.html')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post-create.html'
    fields = ['title', 'content']

