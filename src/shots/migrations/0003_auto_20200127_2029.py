# Generated by Django 3.0.2 on 2020-01-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0002_screenshot_is_fullpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='height',
            field=models.IntegerField(default=768),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='width',
            field=models.IntegerField(default=1366),
        ),
    ]
