from django.db import models
from django.utils import timezone



# Simplied model with foreign keys removed

class OpeningStock(models.Model):
    
    miti = models.DateTimeField(null=True, default=timezone.now)
    quantity = models.PositiveIntegerField(default=34)
    value = models.DecimalField(default=2.5, max_digits=100, decimal_places=2)
    specification = models.CharField(blank=True, null=True, max_length=600, default="Sample Spec")
    remarks = models.TextField(blank=True, null=True, default="Sample remarks")