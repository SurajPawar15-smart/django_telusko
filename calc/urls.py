from django.urls import path
from .views import home, login_view, logout_view, register_view, contact_view


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('contact/', contact_view, name='contact'),
]