from django.views import generic
from django.urls import path, reverse_lazy
from django.contrib.auth import views, mixins
from django.shortcuts import resolve_url
from .models import Post, AppUser
from .forms import LoginForm, ProfileUpdateForm, SignUpForm

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'engineerlog/login.html'

class LogoutView(views.LogoutView, mixins.LoginRequiredMixin):
    template_name = 'engineerlog/logout.html'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('engineerlog:login')
    template_name = 'engineerlog/signup.html'

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

    model = AppUser
    form_class = ProfileUpdateForm
    template_name = 'engineerlog/profile_update.html'

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

    def get_success_url(self):
        return resolve_url('engineerlog:profile', pk=self.kwargs['pk'])