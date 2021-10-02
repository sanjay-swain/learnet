from django.urls import path
from .views import subject_view, chapter_view

urlpatterns = [
    path('', subject_view, name="subjects"),
    path('<str:subject>/', chapter_view, name="chapters")
]
