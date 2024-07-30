from django.shortcuts import render, redirect, get_object_or_404
from .form import *


def index(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, 'blog/index.html', context)


def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('create_post')

    context = {
        'form': form,
        'posts': Blog.objects.all()
    }

    return render(request, 'blog/create_post.html', context)


def create_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_category')

    context = {
        'form': form,
        'categorys': Category.objects.all()
    }

    return render(request, 'blog/create_category.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    context = {
        'post': post,
        'comment_form': CommentForm(),
        'comments': Comment.objects.filter(blog=post)
    }

    return render(request, 'blog/post_detail.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('create_category')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'blog/edit_category.html', {'form': form})


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('create_category')


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('create_post')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('create_post')


def add_comment(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.author = request.user
            comment.save()

    return redirect('post_detail', pk=post.pk)


def category_filter(request):
    id = request.GET.get('id')

    if id is not None:
        category = get_object_or_404(Category, pk=id)
        posts = Blog.objects.filter(category=category)
    else:
        posts = Blog.objects.all()

    context = {
        'posts': posts,
        'all_category': Category.objects.all()
    }

    return render(request, 'blog/category_filter.html', context)


def author_filter(request):
    id = request.GET.get('id')
    if id is not None:
        author = get_object_or_404(User, pk=id)
        posts = Blog.objects.filter(author=author)
    else:
        posts = Blog.objects.all()

    context = {
        'posts': posts,
        'all_author': User.objects.all()
    }

    return render(request, 'blog/author_filter.html', context)
