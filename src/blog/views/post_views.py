from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse

from ..utils import map_field_labels
from ..models import Post
from ..forms import PostForm

from django.urls import reverse_lazy
from django.utils import timezone


LOGIN_ULR = "/user/login/"


def post_detail(request, post_name):
    posts = Post.objects.filter(publish_date__lte=timezone.now(), lang=request.LANGUAGE_CODE, url_name=post_name).all()
    if not posts:
        posts = Post.objects.filter(publish_date__lte=timezone.now(), lang="en", url_name=post_name).all()

    if not posts:
        return render(request, '404.html')

    return render(request, 'blog/post_detail.html', {'post': posts[0]})


class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = LOGIN_ULR
    redirect_field_name = 'blog/post_detail.html'
    permission_required = "blog.add_post"
    permission_denied_message = "You do not have the required permissions!"

    form_class = PostForm
    model = Post

    def form_valid(self, form):
        # Intercept and manipulate form data before saving to the model
        form.instance.last_update_by = self.request.user
        form.instance.last_update_date = timezone.now()
        # Add any additional manipulation here
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = LOGIN_ULR
    redirect_field_name = 'blog/post_detail.html'
    permission_required = "blog.change_post"
    permission_denied_message = "You do not have the required permissions!"

    form_class = PostForm
    model = Post

    def form_valid(self, form):
        # Intercept and manipulate form data before saving to the model
        form.instance.last_update_by = self.request.user
        form.instance.last_update_date = timezone.now()
        # Add any additional manipulation here
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    permission_required = "blog.delete_post"
    permission_denied_message = "You do not have the required permissions!"
