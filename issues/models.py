from django.db import models

class Issue(models.Model):
    ISSUE_TYPES = [
        ('pothole', 'Pothole'),
        ('water', 'Water Leak'),
        ('electricity', 'Electricity Issue'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    description = models.TextField()
    image = models.ImageField(upload_to='issues/', null=True, blank=True)  # ✅ allow no image
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)

    latitude = models.FloatField()
    longitude = models.FloatField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='reported'  # ✅ default status
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.issue_type} - {self.status}"