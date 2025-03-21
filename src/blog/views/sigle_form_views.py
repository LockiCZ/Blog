from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from ..forms import QuoteForm
from ..models import Quote


class CreateQuoteView(CreateView):
    form_class = QuoteForm
    model = Quote
    template_name = "404.html"  # this view is only for post that returns redirect

    def form_invalid(self, form):
        messages.error(self.request, self.request.locals["messages"]["quote_error"])
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.success(self.request, self.request.locals["messages"]["quote_success"])
        # TODO send email
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("home")
