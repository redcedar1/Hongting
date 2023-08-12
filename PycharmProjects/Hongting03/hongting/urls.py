from django.urls import path

from hongting.views import create_user_profile, home, view_user_profiles

urlpatterns = [
    path('create_profile/', create_user_profile, name='create_profile'),
    path('home/', home, name='home'),
    path('홍대축제', create_user_profile, name='홍대축제'),
    path('Result/', view_user_profiles, name='Result')
]