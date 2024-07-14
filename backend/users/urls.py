from rest_framework.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, RegisterUserView, ChangePaswwordView, UpdateProfileView

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUserView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePaswwordView.as_view(), name="auth_change_password"),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),

]


