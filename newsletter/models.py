from django.db import models

# Create your models here.

class Newsletter(models.Model):

    email = models.EmailField( blank=False, max_length=255)
    is_added =models.BooleanField(default=True)

    def __str__(self):
        return self.email
