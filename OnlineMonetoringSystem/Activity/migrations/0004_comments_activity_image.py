# Generated by Django 2.0.5 on 2018-09-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0003_auto_20180907_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments_activity',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
