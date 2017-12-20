from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all()  # offset, limit, step (x)

    q = request.GET.get('q', '')  # request.GET => QueryDict 타입
    if q:
        qs = qs.filter(title__icontains=q)  # where 조건, ILIKE

    return render(request, 'blog/post_list.html', {
        'post_list': qs,
        'q': q,
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def mysum(request, x, y=0, z=0):
    return HttpResponse(int(x) + int(y) + int(z))


def mysum2(request, numbers):
    # result = sum(map(int, numbers.split('/')))
    def fn(number):
        return int(number or 0)
    result = sum(map(fn, numbers.split('/')))
    return HttpResponse(result)


def hello(request, name, age):
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))
