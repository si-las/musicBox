# Generated by Django 2.2.17 on 2021-04-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicboxapp', '0003_auto_20210404_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='Total_Reviews',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='Title',
            field=models.CharField(default='placeholder', max_length=40),
            preserve_default=False,
        ),
    ]