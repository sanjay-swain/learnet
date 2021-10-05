from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Class, Subject, Chapter, Topic, Video


@login_required(login_url="/accounts/login/")
def subject_view(request):
    subject_list = {}
    for subject in Subject.objects.all():
        if len(Chapter.objects.filter(subject_id=subject)) > 1:
            subject_list[subject] = [Chapter.objects.filter(subject_id=subject)[:3]] + \
                                    [Chapter.objects.filter(subject_id=subject)[3:6]]
        else:
            subject_list[subject] = []
    context = {
        'subjects': subject_list
    }
    template_view = 'courses/subjects_page.html'
    return render(request, template_view, context)


@login_required(login_url="/accounts/login/")
def chapter_view(request, subject):
    subject = Subject.objects.get(url=subject)
    chapters = Chapter.objects.filter(subject_id=subject)
    chapter_list = {}
    for chapter in chapters:
        chapter_list[chapter] = [Topic.objects.filter(chapter_id=chapter)[:3]] + \
                                [Topic.objects.filter(chapter_id=chapter)[3:6]]

    context = {
        'all_subjects': Subject.objects.all(),
        'current_subject': subject,
        'chapters': chapter_list
    }
    template_view = 'courses/chapters_page.html'

    return render(request, template_view, context)


@login_required(login_url="/accounts/login/")
def chapter_detail_view(request, subject, chapter):
    current_subject = Subject.objects.get(url=subject)
    current_chapter = Chapter.objects.get(url=chapter)
    all_chapters = Chapter.objects.filter(subject_id=current_subject)
    all_topics = Topic.objects.filter(chapter_id=current_chapter)
    topic_list = {}
    for topic in all_topics:
        topic_list[topic] = Video.objects.filter(topic_id=topic)
    
    context = {
        'all_subjects': Subject.objects.all(),
        'current_subject': current_subject,
        'all_chapters': all_chapters,
        'current_chapter': current_chapter,
        'topics': topic_list
    }
    template_view = 'courses/chapter_detail_page.html'

    return render(request, template_view, context)


@login_required(login_url="/accounts/login/")
def video_detail_view(request, subject, chapter, video):
    current_subject = Subject.objects.get(url=subject)
    current_chapter = Chapter.objects.get(url=chapter)
    current_video = Video.objects.get(url=video)
    current_topic = current_video.topic_id
    all_videos = Video.objects.filter(topic_id=current_topic)
    all_topics = Topic.objects.filter(chapter_id=current_chapter)

    context = {
        'all_videos': all_videos,
        'all_topics': all_topics,
        'current_subject': current_subject,
        'current_chapter': current_chapter,
        'current_topic': current_topic,
        'current_video': current_video
    }
    template_view = 'courses/video_Detail.html'

    return render(request, template_view, context)
