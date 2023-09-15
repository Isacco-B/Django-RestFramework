from django.contrib import admin
from django.urls import path, include
from archive.views import (
    post_detail,
    post_list,
    PostView,
    PostMixingListView,
    PostListView,
    PostDetailView,
    PostDeleteView,
    OwnerDetailView,
    CommentDetailView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("post.urls")),
    # path('api/posts/', PostMixingListView.as_view(), name='post-list'),
    # path('api/post-list/', post_list, name='post-list'),
    # path('api/posts/<int:pk>/', post_detail, name='post-detail'),
    # path("api/posts/", PostListView.as_view(), name="post-list"),
    # path("api/posts/<pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("api/posts/<pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("api/owner/<pk>", OwnerDetailView.as_view(), name="owner-detail"),
    path("api/comment/<pk>", CommentDetailView.as_view(), name="comment-detail"),
]
