# Generated by Django 2.2.3 on 2019-07-10 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangit', '0005_auto_20190708_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='subdjangit',
            name='url',
            field=models.CharField(default='url', max_length=50),
        ),
        migrations.AlterField(
            model_name='subdjangit',
            name='about',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='subdjangit',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
