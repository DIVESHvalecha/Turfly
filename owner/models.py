from django.db import models
from usrs.models import User

# Create your models here.

class Turf(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'owner'})
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='turf_images/', blank=True, null=True)
    amenities = models.CharField(max_length=255, blank=True, help_text='Comma-separated list of amenities')
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'player'})
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending')
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.turf.name} booking by {self.user.name} on {self.date}"
