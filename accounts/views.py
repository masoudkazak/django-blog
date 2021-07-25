from django.db import models
from .models import Profile
from django.views import generic
from .forms import CreateAccountForm, CreateProfileForm
from django.contrib.auth.models import User
from django.urls import reverse


class CreateProfileView(generic.CreateView):
    model = Profile
    template_name = 'create-profile.html'
    form_class = CreateProfileForm

    def get_success_url(self):
        return reverse('blog:homepage')
    
    def get_initial(self):
        return {'user_name': self.request.user}


class CreateAccountView(generic.CreateView):
    model = User
    template_name = 'create-account.html'
    form_class = CreateAccountForm

    def get_success_url(self):
        return reverse('accounts:login')


class ProfileUpdateView(generic.UpdateView):
    model = Profile
    template_name = 'update-profile.html'
    fields = ['bio', 'image_profile', 'phone_number']

    def get_success_url(self):
        return reverse('blog:homepage')
    