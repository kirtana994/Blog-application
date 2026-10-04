from django.shortcuts import render, get_object_or_404,redirect

# Create your views here.
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

# View for displaying the home page with a list of posts also search functionality and pagination
def home(request):

    query = request.GET.get('q', '')

    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/home.html',
        {
            'page_obj': page_obj,
            'query': query
        }
    )

# View for displaying a single post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'post': post})

# Create a new post
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Include request.FILES to handle image uploads

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

# Edit an existing post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})

# Delete a post
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk,author=request.user)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(
        request,
        'blog/post_confirm_delete.html',
        {'post': post}
    )

# View for user signup
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'blog/signup.html')

# View for displaying the posts of the logged-in user
@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_posts.html', {'posts': posts})
