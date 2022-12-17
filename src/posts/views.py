from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from posts.models import BlogPost


# Create your views here.
class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'thumbnail', ]
    template_name = 'posts/blogpost_create.html'


@method_decorator(login_required, name='dispatch')
class BlogPostEdit(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'published', 'thumbnail', ]
    template_name = 'posts/blogpost_edit.html'


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = 'posts/blogpost_detail.html'
    context_object_name = 'post'


@method_decorator(login_required, name='dispatch')
class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy('posts:home')
