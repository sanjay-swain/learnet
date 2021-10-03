from django.urls import path
from .views import chapter_detail_view, subject_view, chapter_view

urlpatterns = [
    path('', subject_view, name="subjects"),
    path('<str:subject>/', chapter_view, name="chapters"),
    path('<str:subject>/<str:chapter>/', chapter_detail_view, name="chapter")
]
