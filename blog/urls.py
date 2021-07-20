from django.urls import path
from .views import (
    PostCreateView,
    PostListView,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    PostCreateView,
    LikeView
)


app_name = 'blog'

urlpatterns = [
    path('home/', PostListView.as_view(), name='homepage'),
    path("home/<str:author>/<str:title>/<int:pk>/", PostDetailView.as_view(), name="detail-post"),
    path('home/<str:author>/<str:title>/<int:pk>/delete/', PostDeleteView.as_view(), name='delete-view'),
    path('home/<str:author>/<str:title>/<int:pk>/update/', PostUpdateView.as_view(), name='update-view'),
    path('home/create-post/', PostCreateView.as_view()),
    path("home/<int:pk>/like/", LikeView, name="like_post"),
]
