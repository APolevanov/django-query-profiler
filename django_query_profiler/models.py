from django.db import models

class QueryProfile(models.Model):
    query = models.TextField()
    execution_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']