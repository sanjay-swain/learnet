from django.urls import path
from .views import login_form, logout_page

urlpatterns = [
    path('login/', login_form, name="login"),
    path('logout/', logout_page, name="logout")
]
