from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Laptop1
from .forms import LaptopModelForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateLaptopView(LoginRequiredMixin,CreateView):
    model = Laptop1
    success_url = reverse_lazy('homepage')
    template_name = 'LaptopApp/form.html'
    form_class = LaptopModelForm


class ListLaptopView(ListView):
    model = Laptop1
    template_name = 'LaptopApp/home.html'
    context_object_name = 'laptops'


class UpdateLaptopView(LoginRequiredMixin,UpdateView):
    model = Laptop1
    form_class = LaptopModelForm
    success_url = reverse_lazy('homepage')
    context_object_name = 'laptop'
    template_name = 'LaptopApp/form.html'


class DeleteLaptopView(LoginRequiredMixin,DeleteView):
    model = Laptop1
    success_url = reverse_lazy('homepage')
    context_object_name = 'laptop'

    template_name = 'LaptopApp/deletepage.html'

