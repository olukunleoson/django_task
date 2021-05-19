from django.urls import path, include
from bloghome.views import homepage, register, contact, Post, add_comment

app_name = 'bloghome'

urlpatterns = [
    
    path('homepage/', homepage, name='homepage'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('contact/', contact, name='contact'),
    path('post/', Post, name='post'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
]