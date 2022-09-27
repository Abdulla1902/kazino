from django.shortcuts import render
from django.http import HttpResponse
from Master_posts.models import Post
# Create your views here.

def main(request):
    posts = Post.objects.all()

    data = {
        'posts': posts
    }

    return render(request, 'main.html', context=data)


def site(request):
    return HttpResponse('<h2><center>Главная<center><h2>')
def contact(request):
    return HttpResponse('<h2><center>Контакты<center><h2>')