from rest_framework import routers
from django.urls import path
from core.user.viewsets import UserViewSet
from core.auth.viewsets import SignUpViewSet, SignInViewSet, RefreshViewSet, ForgotPasswordViewSet, ResetPasswordViewSet
router = routers.SimpleRouter()

router.register(r'auth/signup', SignUpViewSet, basename='auth-signup')
router.register(r'auth/signin', SignInViewSet, basename='auth-signin')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')

router.register(r'user', UserViewSet, basename='user')
urlpatterns = [
    *router.urls,
    path('auth/forgot-password', ForgotPasswordViewSet.as_view(), name='auth-forgotpassword'),
    path('auth/reset-password/<uidb64>/<token>/', ResetPasswordViewSet.as_view(), name='auth-resetpassword'),
] 
