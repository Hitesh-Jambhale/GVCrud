from django.urls import path
from .views import CreateLaptopView, ListLaptopView, UpdateLaptopView, DeleteLaptopView

urlpatterns = [
    path('', ListLaptopView.as_view(), name="homepage"),
    path('create/', CreateLaptopView.as_view(), name="createpage"),
    path('update/<int:pk>/', UpdateLaptopView.as_view(), name='updatepage'),
    path('delete/<int:pk>/', DeleteLaptopView.as_view(), name='deletepage')

]
