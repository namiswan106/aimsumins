from django.db import models
from django.urls import reverse_lazy
from datetime import datetime, timedelta, timezone

from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField
from datetime import datetime

# Create your models here.

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
    ("Internship", "Internship"),
    ("Freelance", "Freelance"),
    ("Work From Home", "Work From Home"),
    ("Remote", "Remote"),
)

class Job(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = HTMLField()
    job_expire = models.CharField(max_length=255)
    job_type= models.CharField(max_length=255, choices=JOB_TYPE,default="Full Time")
    job_role= models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    vacancies = models.IntegerField()
    location_embeded = models.TextField(help_text="Copy and paste embed code from google maps",null=True,blank=True)
    
    
    def get_absolute_url(self):
        return reverse_lazy('web:job-detail', kwargs={'slug': self.slug})
    
    
    
    def get_date(self):
        current_time = datetime.now().replace(tzinfo=None)
        job_date = self.date.replace(tzinfo=None)
        time_difference = current_time - job_date

        # Check if the job was posted today
        if time_difference.days == 0:
            return 'Today'
        
        # Calculate years, months, weeks, and days
        years = time_difference.days // 365
        months = time_difference.days // 30
        weeks = time_difference.days // 7
        days = time_difference.days

        if years > 0:
            return f"{years} {'year' if years == 1 else 'years'} ago"
        elif months > 0:
            return f"{months} {'month' if months == 1 else 'months'} ago"
        elif weeks > 0:
            return f"{weeks} {'week' if weeks == 1 else 'weeks'} ago"
        else:
            return f"{days} {'day' if days == 1 else 'days'} ago"