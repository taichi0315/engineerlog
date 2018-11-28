from django.urls import path, include
from . import views

app_name = 'engineerlog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user/<str:slug>',views.UserDetailView.as_view(), name='user')
]