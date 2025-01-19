from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from FurryFunnies.utils import get_user_obj
from author.forms import AuthorCreateForm, AuthorEditForm, AuthorDeleteForm
from author.models import Author


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'create-author.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    pk_url_kwarg = 'id'
    template_name = 'edit-author.html'
    success_url = reverse_lazy('base')


class AuthorDeleteView(DeleteView):
    model = Author
    form_class = AuthorDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'delete-author.html'
    success_url = reverse_lazy('base')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


class AuthorDetailsView(DetailView):
    model = Author
    pk_url_kwarg = 'id'
    template_name = 'author-author.html'
