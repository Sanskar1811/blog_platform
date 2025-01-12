from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Post
from .forms import PostForm, CommentForm
from django.core.exceptions import ValidationError
from .validators import validate_password  # Import the custom validator


def ucp(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            pw1 = request.POST.get("pw1")
            pw2 = request.POST.get("pw2")

            # Check if the passwords match
            if pw1 != pw2:
                msg = "Passwords did not match"
                return render(request, "registration/ucp.html", {"msg": msg})

            # Validate the new password
            try:
                validate_password(pw1)  # Apply password validation
            except ValidationError as e:
                msg = " ".join(e.messages)
                return render(request, "registration/ucp.html", {"msg": msg})

            # Update the password
            usr = User.objects.get(username=request.user.username)
            usr.set_password(pw1)
            usr.save()
            logout(request)  # Log the user out after password change
            return redirect("ulogin")

        else:
            return render(request, "registration/ucp.html")
    else:
        return redirect("ulogin")

# User home view
def uhome(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(status='published').order_by('-created_at')
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        return redirect("ulogin")

# User signup view
def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    else:
        if request.method == "POST":
            un = request.POST.get("un")
            pw1 = request.POST.get("pw1")
            pw2 = request.POST.get("pw2")

            if pw1 != pw2:
                msg = "Passwords did not match"
                return render(request, "registration/usignup.html", {"msg": msg})

            try:
                validate_password(pw1)  # Validate the password
            except ValidationError as e:
                msg = " ".join(e.messages)
                return render(request, "registration/usignup.html", {"msg": msg})

            try:
                usr = User.objects.get(username=un)
                msg = "User already exists."
                return render(request, "registration/usignup.html", {"msg": msg})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=un, password=pw1)
                usr.save()
                return redirect("ulogin")
        else:
            return render(request, "registration/usignup.html")
        
# User login view
def ulogin(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    else:
        if request.method == "POST":
            un = request.POST.get("un")
            pw = request.POST.get("pw")
            usr = authenticate(username=un, password=pw)
            if usr is None:
                msg = "Invalid Credentials"
                return render(request, "registration/ulogin.html", {"msg": msg})
            else:
                login(request, usr)
                return redirect("uhome")
        else:
            return render(request, "registration/ulogin.html")

# User logout view
def ulogout(request):
    logout(request)
    return redirect("ulogin")

# Post create view
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return render(request, 'blog/post_form.html', {'form': PostForm(), 'post_created': True})

    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

# Post update view
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

# Post delete view
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('/')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

# Post detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'post': post,
        'comments': comments,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
        'comment_form': CommentForm()
    }
    return render(request, 'blog/post_detail.html', context)

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form': form, 'post': post})

# Like post view
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', pk=pk)