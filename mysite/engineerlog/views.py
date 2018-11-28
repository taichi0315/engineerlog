from django.views import generic
from django.urls import path
from django.contrib.auth import views, mixins
from django.shortcuts import resolve_url
<<<<<<< HEAD
from .models import Post, AppUser, Profile
from .forms import LoginForm, ProfileUpdateForm, SignUpForm
=======
from .models import Post, AppUser
from .forms import LoginForm, ProfileUpdateForm
>>>>>>> parent of 42df552... signup

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'engineerlog/login.html'

class LogoutView(views.LogoutView, mixins.LoginRequiredMixin):
    template_name = 'engineerlog/logout.html'

class IndexView(generic.ListView):
    template_name = 'engineerlog/index.html'
    context_object_name = 'posted_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

class ProfileView(generic.DetailView):
    template_name = 'engineerlog/profile.html'
    model = AppUser

class ProfileUpdateView(mixins.UserPassesTestMixin, generic.UpdateView):
    raise_exception = False

    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'engineerlog/profile_update.html'

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

    def get_success_url(self):
        return resolve_url('engineerlog:profile', pk=self.kwargs['pk'])