from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  UpdateView,
                                  DetailView,
                                  CreateView,
                                  DeleteView)
from blog.models import post
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework import permissions
from rest_framework import viewsets


def about(request):
    return render(request, "blog/about.html")


class CreatevieW(LoginRequiredMixin, CreateView):
    model = post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # success_url = "/"


class PostlistvieW(ListView):
    model = post
    ordering = ["-date_posted"]
    # template_name = "blog/home.html"
    paginate_by = 5


class DetailvieW(DetailView):
    model = post


class UpdatevieW(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class DeletevieW(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class UserpostlistvieW(ListView):

    model = post
    template_name = "blog/user_posts.html"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by("-date_posted")


def VueViews(request):
    return render(request, 'blog/Vue.html')


class PostViewset(viewsets.ModelViewSet):
    queryset = post.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
def VueView(request):
    return render(request,'survey/VueView.html')