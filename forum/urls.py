from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Login, Logout e Registro
    path('login/', auth_views.LoginView.as_view(template_name='forum/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # <-- Adicione esta linha!

    # Outras rotas
    path('', views.index, name='index'),
    path('sobre-nos/', views.sobre_nos, name='sobre_nos'),
    path('sobre-empresa/', views.sobre_empresa, name='sobre_empresa'),
]