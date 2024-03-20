from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return self.title
