# Generated by Django 2.2.3 on 2019-07-11 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subdjangit',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('vote', models.IntegerField(default=0)),
                ('post_thread', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangit.Post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='djangit.DjangitUser')),
            ],
        ),
    ]
