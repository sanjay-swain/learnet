from django.urls import path
from .views import subject_view

urlpatterns = [
    path('', subject_view, name="subjects")
]
