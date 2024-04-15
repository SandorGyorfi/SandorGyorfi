from django.db import models

class Contact(models.Model):
    SUBJECT_CHOICES = [
        ('service_request', 'Service Request'),
        ('collaboration', 'Want to Work Together'),
        ('sponsorship', 'Sponsorship'),
        ('complaint', 'Complaint'),
        ('none', 'None Of These'),  
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255, choices=SUBJECT_CHOICES, default='none')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}"  # Display the human-readable version
