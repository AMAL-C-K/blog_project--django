# Generated by Django 3.2.24 on 2024-02-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='body1',
        ),
        migrations.AddField(
            model_name='blog',
            name='body2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='body3',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_image1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_image2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_image3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='cover_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle2',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
