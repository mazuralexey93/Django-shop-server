from django.urls import path

from users.views import UserLoginView, UserRegisterView, UserLogoutView, UserProfileView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),

]
