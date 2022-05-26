from django.db import models


class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_details = models.TextField()
