from django.shortcuts import render , get_object_or_404
from .models import Post



def home(request):
    
    context = { 
        'title': 'Home page',
        'posts': Post.objects.all() 
        }
    return render(request, 'blog/index.html', context )


def about(request):
    return render(request, 'blog/about.html', {'title':'Who Am I !'})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = post.comments.filter(active=True)
    context = {
        'title' : post,
        'post' : post,
        'comments':comment

    } 
    return render(request, 'blog/detail.html', context)   
