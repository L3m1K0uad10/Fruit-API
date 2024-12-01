from django.urls import path
from . import views


urlpatterns = [
    path('', views.fruit_view, name = "fruit_list"),
    path('<int:pk>/', views.fruit_view, name = "fruit_detail"),
    path('create/', views.fruit_view, name = "fruit_create"),
    path('update/<int:pk>/', views.fruit_view, name = "fruit_update"),
    path('delete/<int:pk>/', views.fruit_view, name = "fruit_delete"),
]