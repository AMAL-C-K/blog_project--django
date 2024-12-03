from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Blog


def home(request):
    blog = Blog.objects.all()
    return render(request, "home.html", {'blog': blog})


def create_blog(request):
    if request.method == 'POST':
        title = request.POST['title']
        body1 = request.POST['body1']
        body2 = request.POST['body2']
        body3 = request.POST['body3']
        cover_image = request.FILES['coverimage']
        subtitle1 = request.POST['subtitle1']
        subtitle2 = request.POST['subtitle2']
        blog = Blog.objects.create(title=title, body1=body1, body2=body2, body3=body3, author=request.user, cover_image=cover_image, subtitle1=subtitle1, subtitle2=subtitle2)
        blog.save()
        return redirect('my_blogs')
    return render(request, "create_blog.html")


def view_blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)
    return render(request, "view_blog.html", {'blog': blog})


def delete_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id, author=request.user)
    blog.delete()
    return redirect('my_blogs')


def my_blogs(request):
    blog = Blog.objects.all().filter(author=request.user)
    return render(request, 'my_blogs.html', {'blog': blog})


def view_my_blog(request, blog_id):
    blog = Blog.objects.filter(id=blog_id)
    return render(request, 'view_my_blog.html', {'blog': blog})


def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id, author=request.user)
    return render(request, 'update_blog.html', {'blog': blog})


def update(request, blog_id):
    title = request.POST['title']
    coverimage = request.FILES['coverimage']
    body = request.POST['body1']
    subtitle1 = request.POST['subtitle1']
    body2 = request.POST['body2']
    subtitle2 = request.POST['subtitle2']
    body3 = request.POST['body3']
    blog = Blog.objects.get(id=blog_id, author=request.user)
    blog.title = title
    blog.cover_image = coverimage
    blog.body1 = body
    blog.subtitle1 = subtitle1
    blog.body2 = body2
    blog.subtitle2 = subtitle2
    blog.body3 = body3
    blog.save()
    return redirect('my_blogs')
