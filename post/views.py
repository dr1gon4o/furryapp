from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from FurryFunnies.utils import get_user_obj
from post.forms import PostCreateForm, PostEditForm, PostDeleteForm
from post.models import Post
# Create your views here.


class CreatePostView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class DetailPostView(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'details-post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'id'
    template_name = 'edit-post.html'
    success_url = reverse_lazy('home')


class DeletePostView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'id'
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)
