from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')  # Ensure you have Pillow installed for image fields
    link = models.URLField(blank=True, null=True)  # Optional: link to a detailed service page

    def __str__(self):
        return self.title
