# Generated by Django 2.2.3 on 2019-07-02 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangit', '0002_auto_20190702_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField()),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangit.DjangitUser')),
            ],
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
    ]