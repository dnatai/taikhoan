# Generated by Django 4.2.5 on 2023-10-15 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]