from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=50, verbose_name='Todo Title')
    completed = models.BooleanField(verbose_name='Is Completed')

    def __str__(self):
        return self.title