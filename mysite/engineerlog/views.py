from django.views import generic
from django.urls import path
from django.contrib.auth import views

from .models import Post, AppUser
from .forms import LoginForm

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'engineerlog/login.html'

class IndexView(generic.ListView):
    template_name = 'engineerlog/index.html'
    context_object_name = 'posted_list'

    def get_queryset(self):
        return Post.objects.order_by('-created_at')

class UserDetailView(generic.DetailView):
    template_name = 'engineerlog/user.html'
    model = AppUser
