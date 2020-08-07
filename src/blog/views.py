from django.shortcuts import render , get_object_or_404
from .models import Post, Comment
from .forms import NewComment



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

    #check before save data from comment form
    if request.method == 'POST' :
        comment_form = NewComment(data=request.POST)
        if comment_form.is_valid():
            new_commment = comment_form.save(commit=False)
            new_commment.post = post
            new_commment.save()
            comment_form = NewComment()
    else:
        comment_form = NewComment()
    context = {
        'title' : post,
        'post' : post,
        'comments' : comment,
        'comment_form' : comment_form,
    }

    

    return render(request, 'blog/detail.html', context)   
