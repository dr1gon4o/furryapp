from django import forms
from FurryFunnies.mixins import PlaceholderMixin, ReadOnlyMixin
from author.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorCreateForm(PlaceholderMixin, AuthorBaseForm):
    pass


class AuthorEditForm(PlaceholderMixin, AuthorBaseForm):
    pass


class AuthorDeleteForm(ReadOnlyMixin, AuthorBaseForm):
    pass
