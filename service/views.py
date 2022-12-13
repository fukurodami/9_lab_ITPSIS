from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from service.forms import RegisterUserForm
from .models import Client, Service, Product
from .forms import ClientDataForm
from django.contrib.auth.models import User

class MainView(View):
    def get(self, request):
        serv = Service.objects.all()
        prod = Product.objects.all()
        return render(request, "main_page.html", {'serv': serv, 'prod': prod})


class DataUser(View):
    def get(self, request, pk):
        form = ClientDataForm()
        return render(request, "client.html", {'form': form})

    def post(self, request, pk):
        form = ClientDataForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return HttpResponseRedirect('/')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'reg.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('main_page')

def logout_user(request):
    logout(request)
    return redirect('main_page')





