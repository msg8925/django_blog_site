from django.shortcuts import render
from .models import Post 
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


# function-based views here.
# def home(request):

#     posts = Post.objects.all()

#     context = {
#         'posts': posts
#     }

#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

#def post(request):

#    return render(request, 'blog/post-create.html')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    #template_name = 'blog/post-create.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    fields = ['title', 'content', 'date_posted', 'author']