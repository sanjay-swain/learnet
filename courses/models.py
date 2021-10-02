from django.db import models
from django.conf import settings


class Classes(models.Model):
    user_class = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user_class


class Subjects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    url = models.CharField(max_length=30, unique=True)
    class_id = models.ForeignKey(
        'Classes',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.title


class Chapters(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    subject_id = models.ForeignKey(
        'Subjects',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.title


class Topics(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    chapter_id = models.ForeignKey(
        'Chapters',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return self.title


class Videos(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    video_url = models.CharField(max_length=100)
    chapter_id = models.ForeignKey(
        'Chapters',
        on_delete=models.PROTECT
    )
    topic_id = models.ForeignKey(
        'Topics',
        on_delete=models.PROTECT
    )
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
