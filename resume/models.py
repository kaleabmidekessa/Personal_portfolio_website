from django.db import models
from django.utils import timezone

class About(models.Model):
    name = models.CharField(max_length=100)
    headline = models.CharField(max_length = 100)
    bio = models.TextField()
    resume_attached = models.FileField(upload_to = 'resume/', storage = None)
    social_link = models.URLField(max_length = 200, blank =True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name
        

class Experience(models.Model):
    company_name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 100)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null = True, blank = True)
    achievements = models.TextField(blank = True)
    skill = models.ManyToManyField(Skill, blank = True)

    def __str__(self):
        return self.company_name


class Project(models.Model):
    project_title = models.CharField(max_length = 100)
    description = models.TextField()
    live_demo = models.URLField(max_length = 200, blank = True)
    github_repo = models.URLField(max_length = 200)
    featured_flags = models.BooleanField(default = False)
    skill = models.ManyToManyField(Skill, blank = True)

    def __str__(self):
        return self.project_title