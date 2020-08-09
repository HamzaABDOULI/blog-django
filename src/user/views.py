from django.shortcuts import render, redirect
from .forms import UserCreationForm , LoginForm , UserUpdateForm, ProfileUpdateForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            #messages.success(request,
            #  'Congratulations {} the registration process has been successful'.format(username))
            #ou bien
            messages.success(request,f'Congratulations {new_user} the registration process has been successful')
            return redirect('login')  
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'title':'Register', 'form':form} )


def login_user(request):

    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('profile')
        else:
            messages.warning(request, 'Incorrect username or password.')    
    else:
        form = LoginForm() 
    return render(request, 'user/login.html', {'title':'login', 'form':form} )


def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html', {'title':'logout',} )

@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(author=request.user)
    post_list = Post.objects.filter(author=request.user)
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    posts = Post.objects.filter(author=request.user)
    return render(request, 'user/profile.html', {'title':'profile', 'posts':posts,
     'page':page,'post_liste':post_list,})


def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Profile has been updated')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title':'Edit profile',
        'user_form':user_form,
        'profile_form':profile_form,
    }     
    return render(request, 'user/profile_update.html', context)