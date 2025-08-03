from django.urls import path
from .views import EditProfileAPIView, LoginAPIView, RegisterAPIView, signup_api, get_user_info

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('signup/', signup_api),
    path('user-info/', get_user_info, name='user-info'),
    path('profile/edit/', EditProfileAPIView.as_view(), name='edit-profile'),
]
