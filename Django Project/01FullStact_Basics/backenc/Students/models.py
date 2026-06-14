from django.db import models
# from django.utils import d

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField(max_length=254)
    # created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
