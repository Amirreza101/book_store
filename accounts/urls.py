from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
]
