from django.urls import path
from .views import login_page, logout_page, user_profile

urlpatterns = [
    path('login/', login_page, name="login"),
    path('logout/', logout_page, name="logout"),
    path('profile/<int:index>/', user_profile, name="profile")
]
