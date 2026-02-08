from django.urls import path
from.views import main, user_posts, create_post, view_post

urlpatterns = [
    path('', main),
    path('user/<int:userid>', user_posts),
    path('post/<int:postid>', view_post),
    path('user/create_post', create_post),

]

