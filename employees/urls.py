from django.urls import path
from . import views


urlpatterns = [
    # Employee list view
    path('', views.employee_detail, name='employee_detail'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    
]