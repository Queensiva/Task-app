from django.db import models

class Member(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    duedate=models.DateTimeField()
    priority=models.CharField(max_length=100)
    status = models.CharField(max_length=100)
