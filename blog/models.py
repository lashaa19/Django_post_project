from django.db import models
from django.contrib.auth import get_user_model

user_model = get_user_model()

# Create your models here.
class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey(user_model, on_delete=models.CASCADE)
    time_date = models.DateTimeField(auto_now_add=True)


