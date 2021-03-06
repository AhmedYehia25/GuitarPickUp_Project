# Generated by Django 2.2.5 on 2021-12-31 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('positions', models.TextField(blank=True, null=True)),
                ('path', models.TextField(blank=True, null=True)),
                ('played', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['played'],
            },
        ),
        migrations.CreateModel(
            name='StudentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_id', models.IntegerField(blank=True, null=True)),
                ('Path', models.TextField(blank=True, null=True)),
                ('Excercise_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GuitarPickUp.Excercise')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user_id'],
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, null=True)),
                ('report', models.TextField(blank=True, null=True)),
                ('video_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GuitarPickUp.StudentVideo')),
            ],
            options={
                'ordering': ['video_id'],
            },
        ),
    ]
