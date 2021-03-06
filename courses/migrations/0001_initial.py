# Generated by Django 3.2.7 on 2021-10-02 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('index', models.IntegerField()),
                ('url', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_class', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('index', models.IntegerField()),
                ('url', models.CharField(max_length=30, unique=True)),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('index', models.IntegerField()),
                ('url', models.CharField(max_length=30, unique=True)),
                ('video_url', models.CharField(max_length=100)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('chapter_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.chapter')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('url', models.CharField(max_length=30, unique=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.class')),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.subject'),
        ),
    ]
