from django.shortcuts import render, redirect

from exam.exam_project import get_profile
from exam.exam_project.posts import Post
from exam.exam_project.author.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm


def create_author(request):
    author = get_profile()
    form = CreateProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'author': author,
        'form': form,

    }

    return render(request, 'author/create-author.html', context)


def details_author(request):
    author = get_profile()
    post_count = Post.objects.filter(author=author).count()
    latest_post = Post.objects.order_by('updated_at').last()

    context = {
        'author': author,
        'post_count': post_count,
        'latest_post': latest_post,

    }
    return render(request, 'author/details-author.html', context)


def edit_author(request):
    author = get_profile()

    form = EditProfileForm(instance=author)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=author)
        if form.is_valid():

            form.save()

            return redirect('details-author')

    context = {
        'author': author,
        'form': form,
    }
    return render(request, 'author/edit-author.html', context)


def delete_author(request):
    author = get_profile()

    form = DeleteProfileForm(instance=author)
    if request.method == 'POST':
        author.delete()
        return redirect('index')

    context = {
        'author': author,
        'form': form,
    }
    return render(request, 'author/delete-author.html', context)

