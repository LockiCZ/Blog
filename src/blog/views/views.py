from django.views.generic import (
    TemplateView,
    ListView,
)
from ..utils import map_field_labels
from ..models import Post
from ..forms import QuoteForm

from django.utils import timezone


class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date').all()
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
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
