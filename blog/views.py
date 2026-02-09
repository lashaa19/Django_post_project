from django.contrib.auth import get_user_model
from django.http import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, PostLike, CommentLike

user = get_user_model()

def main(request):
    context = {
        'posts': Post.objects.all().order_by("-pk"),
    }
    return  render(request, 'main.html', context)

def user_posts(request, userid):
    context = {
        'posts': Post.objects.filter(author_id=userid).order_by("-pk"),
        'username': user.objects.get(id=userid).username
    }
    return  render(request, 'main.html', context)

def view_post(request, postid):
    posts = Post.objects.filter(pk=postid)
    post = posts.first() if posts else None
    context = {
        'post': post,
        'comments':Comment.objects.filter(post=post).order_by("-pk"),
        'user_liked': PostLike.objects.filter(post=post, author=request.user).exists()
    }
    return  render(request, 'post.html', context)

def post_comment(request, postid):
    post = Post.objects.filter(pk=postid).first()
    if post and request.method == "POST":
        text = (request.POST.get("text") or "").strip()
        if text:
            Comment.objects.create(
                post=post,
                author=request.user,
                text=text
            )
    return redirect(f"/post/{postid}")

def post_like(request, postid):
    post = Post.objects.filter(pk=postid).first()
    if post and request.method == "POST":
        like = PostLike.objects.filter(post=post, author=request.user)

        if like.exists():
            like.delete()   # снять лайк
        else:
            PostLike.objects.create(post=post, author=request.user)  # поставить лайк

    return redirect(f"/post/{postid}")

def comment_like(request, commentid):
    comment = Comment.objects.filter(pk=commentid).first()
    if comment and request.method == "POST":
        like = CommentLike.objects.filter(comment=comment, author=request.user)

        if like.exists():
            like.delete()   # снять лайк
        else:
            CommentLike.objects.create(comment=comment, author=request.user)  # поставить лайк

    return redirect(f"/post/{comment.post.pk}#comment-{comment.pk}")


@login_required()
def create_post(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Post.objects.create(text=text, author=request.user)
            return redirect("/")
        return render(request, 'create_post.html', context={"error": "No text detected"})
    return  render(request, 'create_post.html',)


