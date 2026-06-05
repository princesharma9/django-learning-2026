from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
 
 
class ChaiVarity(models.Model):
    CHAI_VARITY_CHOICE = [
        ('MS' , 'Masala'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_VARITY_CHOICE)
    description = models.TextField(default='')
    def __str__(self):
        return self.name
    

#One to many

class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete= models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


