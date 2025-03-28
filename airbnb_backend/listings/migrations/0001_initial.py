# Generated by Django 5.1.7 on 2025-03-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirbnbListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price_per_night', models.FloatField()),
                ('ratings', models.FloatField(blank=True, null=True)),
                ('reviews', models.IntegerField(blank=True, null=True)),
                ('amenities', models.JSONField()),
                ('image_urls', models.JSONField()),
            ],
        ),
    ]
