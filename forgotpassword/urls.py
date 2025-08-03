from django.urls import path
from . import views

urlpatterns = [
    path('password-reset/', views.password_reset_request, name='password_reset'),
    path('password-reset-confirm/', views.password_reset_confirm, name='password_reset_confirm_api'),  # API call (optional)
    path('reset-password/', views.reset_password_form, name='reset_password_form'),  # NEW HTML Form
    path('reset-password-submit/', views.reset_password_submit, name='reset_password_submit'),  # NEW Submit handler
]
