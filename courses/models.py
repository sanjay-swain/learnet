from django.db import models
from django.conf import settings


class Class(models.Model):
    user_class = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user_class


class Subject(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    url = models.CharField(max_length=30, unique=True)
    class_id = models.ForeignKey(
        'Class',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.class_id.user_class}'


class Chapter(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    subject_id = models.ForeignKey(
        'Subject',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.subject_id.title}'


class Topic(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    chapter_id = models.ForeignKey(
        'Chapter',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.chapter_id.title}'


class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    video_url = models.CharField(max_length=300)
    chapter_id = models.ForeignKey(
        'Chapter',
        on_delete=models.PROTECT
    )
    topic_id = models.ForeignKey(
        'Topic',
        on_delete=models.PROTECT
    )
    author_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.chapter_id.title}'
