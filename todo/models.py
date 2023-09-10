from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    #!!! mandatory fields for each model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task