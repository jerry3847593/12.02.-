from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    post_list = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': post_list})

def detail(request, post_id):
    # post가 없으면 404 에러를 보이시오
    post = get_object_or_404(Post, pk = post_id)

    return render(request, "blog/detail.html", {"post": post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect("detail", post_id=post.pk)
    else:
        form = PostForm()
        return render(request, "blog/new.html", {"form":form})

