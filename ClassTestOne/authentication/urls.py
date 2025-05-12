from django.urls import path
from . import views

urlpatterns = [
    path('', views.userCreate, name='register'),
    path('login/', views.userLogin, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('changewithold/', views.change_with_old, name='changewithold'),
    path('changewithoutold/', views.without_old, name='changewithoutold'),
    path('success/', views.success, name='success')
]
