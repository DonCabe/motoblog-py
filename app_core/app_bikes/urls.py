from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('contacto/', views.contacto, name='contacto'),
]