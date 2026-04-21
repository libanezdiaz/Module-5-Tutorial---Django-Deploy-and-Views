from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #return to the requester the hml page anf the data they are asking
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts}) 

#create a post detail function to search by id and brag ONE item or return a 404 if not
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

