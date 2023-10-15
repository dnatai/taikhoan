from django.urls import path
from .views import HomeView, ArticleDetailView, CreatePostView, EditPostView,DeletePostView, AddCommentView,DraftView,AboutUs,LikeView

urlpatterns = [
    path('',HomeView.as_view(),name='HomeView'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="ArticalDetail"),
    path('create_post/',CreatePostView.as_view(), name = 'CreatePostView'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="EditPostView"),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name="DeletePostView"),
    path('artical/<int:pk>/comment/',AddCommentView.as_view(), name = 'AddCommentView'),
    path('draft/',DraftView.as_view(),name="draft"),
    path('aboutus/',AboutUs,name="about"),
    path('like/<int:pk>', LikeView, name='like_post'),
]
