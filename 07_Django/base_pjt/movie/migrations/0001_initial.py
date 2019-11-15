# Generated by Django 2.1.5 on 2019-02-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_eng', models.CharField(max_length=100)),
                ('audience', models.ImageField(default=0, upload_to='')),
                ('open_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('watch_grade', models.CharField(max_length=100)),
                ('score', models.FloatField(default=0.0)),
                ('poster_url', models.TextField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
