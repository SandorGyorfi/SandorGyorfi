from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(default='No short description provided.')
    description = models.TextField()
    home_description = models.TextField(default='Brief overview for home page.', help_text='A concise description for the home page.')
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
