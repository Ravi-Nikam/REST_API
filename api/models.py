from django.db import models

# Create your models here.
class Account(models.Model):
    Name = models.CharField(max_length =100)
    Mobile = models.PositiveIntegerField()

    def __str__(self):
        return self.Name