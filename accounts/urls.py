from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('logout/', views.LogoutView.as_view(), name='logout-page'),
    path('forget-password/',views.ForgetPasswordView.as_view(),name='forgot-password'),
    path('reset-password/<active-code>', views.ResetPasswordView.as_view(), name='reset-password'),
    path('active-code/<email_active_code>',views.ActivateAccountView.as_view(),name='email-active-code'),
]
