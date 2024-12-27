from django.urls import path
from .views import UserLoginView, ProfileView, UserListView, UserCreateView, UserUpdateView, UserDeleteView, CustomPasswordChangeView

app_name = "app_users"

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
]
