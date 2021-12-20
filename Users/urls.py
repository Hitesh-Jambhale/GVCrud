from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import user_register_view
from django.urls import reverse_lazy

urlpatterns = [
    path('login/', LoginView.as_view(template_name='Users/login.html'), name='loginpage'),
    path('logout/', LogoutView.as_view(template_name='Users/logout.html'),
         name='logoutpage'),
    path('register/', user_register_view, name='registerpage')
]
