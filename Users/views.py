from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def user_register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginpage')
    return render(request, template_name='Users/form.html', context={'form': form})
