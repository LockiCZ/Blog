from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse

from ..utils import map_field_labels
from ..models import Post, Comment, Quote
from ..forms import PostForm, CommentForm, QuoteForm

from django.urls import reverse_lazy
from django.utils import timezone

from django.contrib import messages


# Create your views here.

LOGIN_ULR = "/user/login/"


class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').all()
        context["form"] = map_field_labels(QuoteForm(), context["view"].request.locals["quote_form"])
        return context


class ServicesView(TemplateView):
    template_name = 'blog/services.html'


class ContactView(TemplateView):
    template_name = 'blog/contact.html'


class FaqView(TemplateView):
    template_name = 'blog/FAQ.html'


class BlogView(ListView):
    model = Post
    template_name = 'blog/blog.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post


class CreateQuoteView(CreateView):
    form_class = QuoteForm
    model = Quote
    template_name = "404.html"  # this view is only for post that returns redirect

    def form_invalid(self, form):
        messages.error(self.request, self.request.locals["messages"]["quote_error"])
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.success(self.request, self.request.locals["messages"]["quote_success"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home")


class CreatePostView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    login_url = LOGIN_ULR
    redirect_field_name = 'blog/post_detail.html'
    permission_required = "blog.add_post"
    permission_denied_message = "You do not have the required permissions!"

    form_class = PostForm
    model = Post


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = LOGIN_ULR
    redirect_field_name = 'blog/post_detail.html'
    permission_required = "blog.change_post"
    permission_denied_message = "You do not have the required permissions!"

    form_class = PostForm
    model = Post


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    permission_required = "blog.delete_post"
    permission_denied_message = "You do not have the required permissions!"


class DraftListView(LoginRequiredMixin, ListView):
    login_url = LOGIN_ULR
    redirect_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


#########################################################
#########################################################

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
