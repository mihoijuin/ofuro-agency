# Generated by Django 2.0.8 on 2018-11-14 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofuro', '0006_auto_20181111_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ofuroresult',
            name='image_url_L',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ofuroresult',
            name='image_url_S',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]