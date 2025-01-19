
from django.urls import path, include
from post import views

urlpatterns = [
    path('posts/', views.CreatePostView.as_view(), name='post_create_page'),
    path('posts/<int:post_id>/', include([
        path('edit/', views.DetailPostView.as_view(), name='post_edit_page'),
        path('details/', views.EditPostView.as_view(), name='post_details_page'),
        path('delete/', views.DeletePostView.as_view(), name='post_delete_page'),
    ]))
]
