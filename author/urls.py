from django.urls import path
from author import views

urlpatterns = [
    path('author/', views.AuthorCreateView.as_view(), name='author_create_page'),
    path('author/', views.AuthorDetailsView.as_view(), name='author_details_page'),
    path('author/', views.AuthorEditView.as_view(), name='author_edit_page'),
    path('author/', views.AuthorDeleteView.as_view, name='author_delete_page'),
]