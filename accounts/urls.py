from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateProfileView, CreateAccountView, ProfileUpdateView


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('create-profile/', CreateProfileView.as_view(), name='create-profile'),
    path('create-account/', CreateAccountView.as_view(), name='create-account'),
    path('<int:pk>/update-profile/', ProfileUpdateView.as_view(), name='update-profile'),
]

