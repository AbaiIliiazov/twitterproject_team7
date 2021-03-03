from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SearchResultsView,
    UserPostListView,
    FollowsListView,
    FollowersListView)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/del/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),
]