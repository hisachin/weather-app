from django.db import models
from django.utils import timezone

# Create your models here.
class City(models.Model):
	city_name = models.CharField(max_length=200)
	created_date = models.DateTimeField(
            default=timezone.now)
		