from django.shortcuts import render


posts = [
    {
        'title':'The first post',
        'content':' first text ',
        'post_date':'05/8/2020',
        'auther':'Hamza ABDOULI' ,
    },
    {
        'title':'The second post',
        'content':' text 2 ',
        'post_date':'04/7/2020',
        'auther':'Ghassen ABDOULI' ,
    },
    {
        'title':'The third post',
        'content':' text ',
        'post_date':'03/7/2020',
        'auther':'Iheb ABDOULI' ,
    },
    {
        'title':'The fourth post',
        'content':' text ',
        'post_date':'02/7/2020',
        'auther':'Iheb ABDOULI' ,
    },
    {
        'title':'The fifth post',
        'content':'last text ',
        'post_date':'01/6/2020',
        'auther':'Hamza ABDOULI' ,
    }
]

def home(request):
    
    context = { 
        'title': 'Home page',
        'pos': posts 
        }
    return render(request, 'blog/index.html', context )


def about(request):
    return render(request, 'blog/about.html', {'title':'Who Am I !'})
