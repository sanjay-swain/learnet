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
