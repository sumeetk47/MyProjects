from django.db import models

class books(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length = 100)
    rating = models.CharField(max_length = 100)
    class Meta:
        db_table="Books"
