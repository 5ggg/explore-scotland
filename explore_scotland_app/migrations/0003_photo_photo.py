# Generated by Django 3.0.3 on 2020-03-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore_scotland_app', '0002_auto_20200315_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]