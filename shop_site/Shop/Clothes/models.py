from django.db import models
from django.utils import timezone
# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=40)
    for_men = models.BooleanField()
    category = models.CharField(max_length=20)
    size = models.CharField(max_length=5)
    price = models.FloatField()
    images = models.ImageField(upload_to='clothes')
    pub_date = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.name
