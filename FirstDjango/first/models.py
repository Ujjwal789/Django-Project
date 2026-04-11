from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

#one to many relationship
class Review(models.Model):
    chaivarity = models.ForeignKey(chaivarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars')
        ]
    )
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def _str__(self):
        return f'Review by {self.user.username} for {self.chaivarity.name}'
    
#many to many relationship    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chaivarity = models.ManyToManyField(chaivarity)
    date_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Order by {self.user.username} on {self.date_ordered}'
    
class store(models.Model):
    name = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    chaivarity = models.ManyToManyField(chaivarity)
    date_opened = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name    
    
# one to one relationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profiles/')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Profile of {self.user.username}'    