from django.db import models
from usrs.models import User
from owner.models import Turf

# Create your models here.

class PlayerBooking(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'player'})
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending')
    payment_status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.turf.name} booking by {self.player.name} on {self.date}"
