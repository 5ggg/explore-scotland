# Generated by Django 3.0.3 on 2020-03-01 19:52

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
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=256)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('categories', models.CharField(max_length=256)),
                ('tags', models.CharField(max_length=256)),
                ('likes', models.ManyToManyField(related_name='photos_liked', to='explore_scotland_app.Profile')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos_uploaded', to='explore_scotland_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=256)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_comments', to='explore_scotland_app.Comment')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_posted', to='explore_scotland_app.Profile')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photo_comments', to='explore_scotland_app.Photo')),
            ],
        ),
    ]