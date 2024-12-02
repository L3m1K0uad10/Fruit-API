from django.urls import path
from . import views


urlpatterns = [
    path('', views.FruitListCreateAPIView.as_view(), name = "fruit_list"),
    path('<int:pk>/', views.FruitDetailAPIView.as_view(), name = "fruit_detail"),
    path('', views.FruitListCreateAPIView.as_view(), name = "fruit_create"),
    path('<int:pk>/', views.FruitUpdateAPIView.as_view(), name = "fruit_update"),
    path('<int:pk>/', views.FruitDestroyAPIView.as_view(), name = "fruit_delete"),
]