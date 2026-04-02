from django.db import models


class Experience(models.Model):
    duration = models.CharField(max_length=50)  # e.g., "Nov 2025 – Present"
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    stack = models.CharField(max_length=100)  # e.g., "Flutter, Django"

    def __str__(self):
        return f"{self.role} at {self.company}"


class Project(models.Model):
    title = models.CharField(max_length=100)
    features = models.TextField()  # Detailed features
    stack = models.CharField(max_length=100)  # e.g., "Python, Django, PostgreSQL"
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Certification(models.Model):
    title = models.CharField(max_length=150)
    authority = models.CharField(max_length=100)  # e.g., "TCS iON", "NPTEL"

    def __str__(self):
        return self.title