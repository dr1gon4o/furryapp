from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import BaseFormView
from FurryFunnies.utils import get_user_obj
from author.forms import AuthorCreateForm
from post.models import Post


class BasePage(ListView, BaseFormView):
    model = Post
    form_class = AuthorCreateForm
    success_url = reverse_lazy('base')

    def get_template_names(self):
        author = get_user_obj()

        if author:
            return ['base-with-author.html']

        return ['base-no-author.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
