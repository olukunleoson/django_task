from django.urls import path, include
from bloghome.views import homepage, register

app_name = 'bloghome'

urlpatterns = [
    
    path('homepage/', homepage, name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]