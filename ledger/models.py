from datetime import datetime
from django.db import models
from django.urls import reverse

class TaskGroup(models.Model):
    name = models.CharField(max_length=50)

class Task(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=False)
    taskgroup = models.ForeignKey(
        TaskGroup,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return '{}: due on {} unit(s)'.format(self.name, self.due_date)
    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.name)])
    @property
    def is_due(self):
        return datetime.now() >= self.due_date
    
    class Meta:
        ordering = ['due_date'] # order by due date ascending order
        unique_together = ['due_date', 'name'] # Don't create a duplicate task
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
