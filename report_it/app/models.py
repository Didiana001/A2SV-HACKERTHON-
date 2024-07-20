from django.contrib.auth.models import User
from django.db import models


# Report model

class Report(models.Model):
    REPORT_TYPES = [
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
        ('Type3', 'Type 3'),
        # Add more report types as needed
    ]
    
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    description = models.TextField()
    image = models.ImageField(upload_to='report_images/', blank=True, null=True)
    video = models.FileField(upload_to='report_videos/', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Authorities model

class Authority(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='authority_logos/')
    contact = models.CharField(max_length=100)
    addresses = models.JSONField()  # This will allow you to store multiple addresses in JSON format

    def __str__(self):
        return self.name