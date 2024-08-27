from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.job_list_view, name='job_list'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
]
