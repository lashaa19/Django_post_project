from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post

def main(request):
    context = {
        'posts': Post.objects.all().order_by("-pk"),
    }
    return  render(request, 'main.html', context)

def user_posts(request, userid):
    context = {
        'posts': Post.objects.filter(author_id=userid).order_by("-pk"),
    }
    return  render(request, 'main.html', context)

@login_required()
def create_post(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Post.objects.create(text=text, author=request.user)
            return redirect("/")
        return render(request, 'create_post.html', context={"error": "No text detected"})
    return  render(request, 'create_post.html',)


