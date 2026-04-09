from django.db import models
from django.utils import timezone

# Create your models here.
class chaivarity(models.Model):
    chai_type_choices = [
      ('ml', 'masala'),
      ('gr', 'ginger'),
      ('el', 'elichi'),
      ('ma', 'macha'),
    
    ]
    name = models.CharField(max_length=1000)
    image =models.ImageField(upload_to='first/')
    date_added =models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=chai_type_choices)
    descriptions = models.TextField(default='')


    def __str__(self):
        return self.name
    



