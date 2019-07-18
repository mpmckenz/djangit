# Generated by Django 2.2.3 on 2019-07-18 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangitUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subdjangit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(default='', max_length=50)),
                ('about', models.TextField(blank=True, max_length=75, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('moderator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='moderator', to='djangit.DjangitUser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('title', models.CharField(max_length=150)),
                ('body', models.TextField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url', models.CharField(max_length=200)),
                ('subdjangit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangit.Subdjangit')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangit.DjangitUser')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticed', models.BooleanField(default=False)),
                ('notify_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangit.DjangitUser')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangit.Post')),
            ],
        ),
        migrations.AddField(
            model_name='djangituser',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, related_name='subscriptions', to='djangit.Subdjangit'),
        ),
        migrations.AddField(
            model_name='djangituser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_score', models.IntegerField(db_index=True, default=0)),
                ('num_vote_up', models.PositiveIntegerField(db_index=True, default=0)),
                ('num_vote_down', models.PositiveIntegerField(db_index=True, default=0)),
                ('text', models.TextField(default='', max_length=1000)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('post', models.ForeignKey(on_delete=True, related_name='comments', to='djangit.Post')),
                ('user', models.ForeignKey(on_delete=False, to='djangit.DjangitUser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
