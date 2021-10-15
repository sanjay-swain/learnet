from django.urls import path
from .views import chapter_detail_view, subject_view, chapter_view, video_detail_view, topic_view

urlpatterns = [
    path('', subject_view, name="subjects"),
    path('<str:subject>/', chapter_view, name="chapters"),
    path('<str:subject>/<str:chapter>/', chapter_detail_view, name="chapter"),
    path('redirect/<str:chapter>/<str:topic>/', topic_view),
    path('<str:subject>/<str:chapter>/<str:video>/', video_detail_view, name="video")
]
