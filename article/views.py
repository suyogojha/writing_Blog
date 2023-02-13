from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify
from writer.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def index(request):
    posts = Post.objects.all()
    page = request.GET.get('page')
    numbers = 3
    paginator = Paginator(posts, numbers)

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)
    tags = Tag.objects.all()
    context = {'posts': posts, 'paginator': paginator, 'tags': tags}
    return render(request, 'article/index.html', context)


  
def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    form = CommentForm()
    if request.method=='POST':
        # check whether the user is login or not to comment 
            if request.user.is_authenticated:
                form = CommentForm(request.POST)
                if form.is_valid():
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()
                    return redirect('detail', slug=post.slug)
            else:
                return redirect('signin')
    context = {'post': post, 'posts':posts, 'form': form}
    return render(request, 'article/detail.html', context)



def createPost(request):
    profile = request.user.profile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = profile
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, 'Your article was created successfully')
            return redirect('account')
    context = {'form': form}
    return render(request, 'article/create.html', context)

def editPost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('detail', slug=post.slug)
    context = {'form': form}
    return render(request, 'article/create.html', context)


def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method=='POST':
        post.delete()
        messages.info(request, 'Post deleted successfully')
        return redirect('account')
    context = {'form': form}
    return render(request, 'article/delete.html', context)

def followers(request, pk):
    profile = Profile.objects.get(id=pk)
    follower = request.user.profile
    return redirect(detail, pk = profile.id)

def tagPage(request, slug):
    tag = Tag.objects.get(slug=slug)
    context = {'tag': tag}
    return render(request, 'article/tag.html', context)






    
