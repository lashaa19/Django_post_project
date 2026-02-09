from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)
    time_date = models.DateTimeField(auto_now_add=True)

    def likes_count(self):
        return PostLike.objects.filter(post=self).count()

class Comment(models.Model):
    post = models. ForeignKey(Post, on_delete=models. CASCADE)
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)
    text = models. TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Like(models. Model):
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)

class PostLike(Like):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")

class CommentLike(Like):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)