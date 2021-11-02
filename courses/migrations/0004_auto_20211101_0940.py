# Generated by Django 3.2.8 on 2021-11-01 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20211015_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='chapter_id',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='chapter_id',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='topic_id',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='class_id',
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
