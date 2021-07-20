from .forms import PostCreateForm
from .models import Post
from django.views import generic
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:detail-post', args=(post.id,)))


class PostListView(generic.ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    ordering = ['-create_post']
    paginate_by = 5


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = 'post'

    def get_context_data(self,*args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['total_likes'] = total_likes
        return context


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "post_delete.html"

    def get_success_url(self):
        return reverse('blog:homepage')
    

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title', 'body', 'status', 'category']

    def get_success_url(self):
        return reverse('blog:homepage')


class PostCreateView(generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post_create.html'
    
    def get_success_url(self):
        return reverse('blog:homepage')

    def get_initial(self):
        return {'author': self.request.user}


