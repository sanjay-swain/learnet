from django.shortcuts import render
from .models import Class, Subject, Chapter, Topic, Video


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
