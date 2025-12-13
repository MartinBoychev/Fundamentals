from django.shortcuts import render

from exam.exam_project import get_profile, get_all_records


# Create your views here.

def index(request):
    author = get_profile()
    context = {'author': author}
    return render(request, template_name='common/index.html', context=context)


def dashboard(request):
    author = get_profile()
    posts = get_all_records()
    context = {
        'author': author,
        'posts': posts,
    }
    return render(request, 'common/dashboard.html', context)
