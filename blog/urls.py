from django.urls import path
from.views import main, user_posts, create_post

urlpatterns = [
    path('', main),
    path('user/<int:userid>', user_posts),
    path('user/create_post', create_post),
]

