from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/', views.vote, name='vote'),
    path('create/<int:pk>', views.create, name='create'),
    path('seal', views.seal, name='seal'),
    path('verify', views.verify, name='verify'),
    path('results', views.result, name='result'),
    path('register',views.register,name='register'),
    path('otp',views.otp,name='otp'),
    path('login',views.signin,name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/', views.reset_password, name='reset_password'),
]