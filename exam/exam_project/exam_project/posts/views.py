from django.shortcuts import render, redirect

from exam.exam_project import get_profile
from exam.exam_project.posts.forms import CreatePostForm, EditPostForm, DeletePostForm
from exam.exam_project.posts import Post


def add_post(request):
    author = get_profile()
    form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect('dashboard')

    context = {
        'author': author,
        'form': form,
    }

    return render(request, 'post/create-post.html', context)


def details_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    author = get_profile()

    context = {
        'post': post,
        'author': author,

    }
    return render(request, 'post/details-post.html', context)


def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    author = get_profile()

    form = EditPostForm(instance=post)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'post': post,
        'form': form,
        'author': author,
    }
    return render(request, 'post/edit-post.html', context)


def delete_post(request, post_id):
    author = get_profile()
    post = Post.objects.get(pk=post_id)

    form = DeletePostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    context = {
        'post': post,
        'form': form,
        'author': author,
    }
    return render(request, 'post/delete-post.html', context)