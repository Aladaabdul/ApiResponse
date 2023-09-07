from django.db import models

# Create your models here.

class ApiResponse(models.Model):
    slack_name = models.CharField(max_length=200)
    current_day = models.CharField(max_length=200)
    utc_time = models.DateTimeField()
    track = models.CharField(max_length=200)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
    status_code = models.PositiveSmallIntegerField(default=200)