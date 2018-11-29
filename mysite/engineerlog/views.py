from django.views import generic
from django.urls import path, reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import views, mixins
from django.shortcuts import resolve_url
from .models import Post, AppUser
from .forms import LoginForm, ProfileUpdateForm, SignUpForm, PostCreateForm

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'engineerlog/login.html'

class LogoutView(views.LogoutView, mixins.LoginRequiredMixin):
    template_name = 'engineerlog/logout.html'

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'engineerlog/signup.html'
    success_url = reverse_lazy('engineerlog:login')

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

    def form_valid(self, form):
        form.instance.icon = self.object.icon
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('engineerlog:profile', pk=self.kwargs['pk'])

class PostCreateView(generic.CreateView):
    form_class = PostCreateForm
    success_url = reverse_lazy('engineerlog:index')
    template_name = 'engineerlog/post_create.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)