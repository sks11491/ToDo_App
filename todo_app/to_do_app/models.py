from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.text)
    class Meta:
        verbose_name_plural = "To Do List"