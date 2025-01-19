from django import forms
from FurryFunnies.mixins import PlaceholderMixin, ReadOnlyMixin
from post.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)


class PostCreateForm(PlaceholderMixin, PostBaseForm):
    pass


class PostEditForm(PlaceholderMixin, PostBaseForm):
    pass


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    pass
