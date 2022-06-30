from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts', views.posts_view),
    path('posts/<int:name_post>', views.post_view_by_number),
    path('posts/<str:name_post>', views.post_view),
]
