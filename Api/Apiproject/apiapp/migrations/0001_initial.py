# Generated by Django 4.2.5 on 2023-09-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_name', models.CharField(max_length=200)),
                ('current_day', models.CharField(max_length=200)),
                ('utc_time', models.DateTimeField()),
                ('track', models.CharField(max_length=200)),
                ('github_file_url', models.URLField()),
                ('github_repo_url', models.URLField()),
                ('status_code', models.PositiveSmallIntegerField(default=200)),
            ],
        ),
    ]
