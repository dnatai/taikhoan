from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Comment
from .form import PostFrom, CommentFrom
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
def home(request):
    return render(request, 'home.html')

class HomeView(ListView):
    paginate_by = 3
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    

class DraftView(ListView):
    model = Post
    template_name = 'draft.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'
    
    def get_context_data(self, *args ,**kwargs):
        context = super(ArticleDetailView,self).get_context_data(*args ,**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class CreatePostView(CreateView):
    model = Post
    form_class = PostFrom
    template_name = 'create_post.html'
    success_url = reverse_lazy('draft')

class AddCommentView(CreateView):
    model = Comment
    ordering = ['-id']
    template_name = 'add_comment.html'
    form_class = CommentFrom
    success_url = reverse_lazy('HomeView')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'body','draft']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('HomeView')

def AboutUs(request):
    
   return render(request,"aboutus.html")

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked= False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('ArticalDetail', args=[str(pk)]))

def CommentView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    return HttpResponseRedirect(reverse('ArticalDetail', args=[str(pk)]))


