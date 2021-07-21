from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    PostCreateView,
    LikeView,
    CommentCreateView
)


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='homepage'),
    path("<str:author>/<str:title>/<int:pk>/", PostDetailView.as_view(), name="detail-post"),
    path('<str:author>/<str:title>/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-view'),
    path('<str:author>/<str:title>/<int:pk>/update/', PostUpdateView.as_view(), name='update-view'),
    path('create-post/', PostCreateView.as_view()),
    path("<int:pk>/like/", LikeView, name="like_post"),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='addcomment')
]
