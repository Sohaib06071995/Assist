# Generated by Django 2.0.5 on 2018-09-07 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity', '0002_auto_20180907_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_activity',
            name='commented_by',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
