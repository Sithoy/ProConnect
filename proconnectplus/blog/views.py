# blog/views.py

from django.shortcuts import render
from .models import Post
from .forms import PostForm

# List Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

# Create Post

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:post_list')  # Redirect to the blog post list view after saving
    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})