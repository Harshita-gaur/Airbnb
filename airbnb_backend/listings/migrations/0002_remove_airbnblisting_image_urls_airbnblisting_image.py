# Generated by Django 5.1.7 on 2025-03-17 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airbnblisting',
            name='image_urls',
        ),
        migrations.AddField(
            model_name='airbnblisting',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='listings/'),
        ),
    ]
