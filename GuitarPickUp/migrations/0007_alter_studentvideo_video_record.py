# Generated by Django 4.0.3 on 2022-05-28 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GuitarPickUp', '0006_merge_20220528_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentvideo',
            name='video_record',
            field=models.FileField(null=True, upload_to='records'),
        ),
    ]
