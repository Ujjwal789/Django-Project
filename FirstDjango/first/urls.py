from django.urls import path
from . import views

urlpatterns = [
    path('', views.first, name='all_Home'),
    path('<int:chai_id>/', views.chai_details, name='chai_details'),
    path('first/', views.first, name='chai_list'),
    path('chai_store/', views.store_view, name='chai_store'),
]