from django.urls import path
from . import views


urlpatterns = [
    path('', views.FruitListCreateAPIView.as_view(), name = "fruit_list"),
    path('<int:pk>/', views.FruitDetailAPIView.as_view(), name = "fruit_detail"),
    path('create/', views.FruitListCreateAPIView.as_view(), name = "fruit_create"),
    path('update/<int:pk>/', views.FruitUpdateAPIView.as_view(), name = "fruit_update"),
    path('delete/<int:pk>/', views.FruitDestroyAPIView.as_view(), name = "fruit_delete"),
]