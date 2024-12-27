from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm, ProfileEditForm
from django.shortcuts import get_object_or_404


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'app_users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('app_users:profile')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'app_users/profile.html'

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'app_users/user_list.html'
    context_object_name = 'users'

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "app_users/user_create.html"
    success_url = reverse_lazy('app_users:user_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "app_users/user_edit.html"
    success_url = reverse_lazy('app_users:profile')

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "app_users/user_delete.html"
    success_url = reverse_lazy('app_users:user_list')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'app_users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Crea un perfil si no existe para evitar errores
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        context['profile'] = profile
        return context

def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('app_users:profile')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
    return render(request, 'app_users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'app_users/password_change.html'
    success_url = reverse_lazy('app_users:profile')