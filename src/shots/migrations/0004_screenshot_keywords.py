# Generated by Django 3.0.2 on 2020-01-27 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0003_auto_20200127_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='keywords',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
