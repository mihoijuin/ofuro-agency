# Generated by Django 2.0.8 on 2018-11-10 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ofuro', '0002_guestintroduce_introduce_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestintroduce',
            name='introduce_text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='guestintroduce',
            name='introduce_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]