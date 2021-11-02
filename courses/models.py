from django.db import models
from django.conf import settings


class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150, null=True, blank=True)
    url = models.CharField(max_length=30, unique=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    subject = models.ForeignKey(
        'Subject',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.subject.title}'


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    chapter = models.ForeignKey(
        'Chapter',
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.chapter.title}'


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=150, null=True, blank=True)
    index = models.IntegerField()
    url = models.CharField(max_length=30, unique=True)
    video_url = models.CharField(max_length=300)
    chapter = models.ForeignKey(
        'Chapter',
        on_delete=models.PROTECT
    )
    topic = models.ForeignKey(
        'Topic',
        on_delete=models.PROTECT
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self) -> str:
        return f'{self.title} - {self.chapter.title}'
