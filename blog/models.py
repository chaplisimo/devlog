from django.db import models


# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
# author =
