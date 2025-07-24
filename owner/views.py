from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Turf, Booking
from usrs.models import User
from django import forms
from django.contrib import messages

# Create your views here.

def dashboard(request):
    if not hasattr(request.user, 'user_type') or request.user.user_type != 'owner':
        return redirect('account_login')  # or some error page
    turfs = Turf.objects.filter(owner=request.user)
    bookings = Booking.objects.filter(turf__owner=request.user).select_related('turf', 'user')
    context = {
        'turfs': turfs,
        'bookings': bookings,
    }
    return render(request, 'owner/dashboard.html', context)

class TurfForm(forms.ModelForm):
    class Meta:
        model = Turf
        fields = ['name', 'location', 'description', 'image', 'amenities', 'price_per_hour', 'available_time_slots']

@login_required
def add_turf(request):
    if not hasattr(request.user, 'user_type') or request.user.user_type != 'owner':
        return redirect('account_login')
    if request.method == 'POST':
        form = TurfForm(request.POST, request.FILES)
        if form.is_valid():
            turf = form.save(commit=False)
            turf.owner = request.user
            turf.save()
            messages.success(request, 'Turf added successfully!')
            return redirect('owner:owner_dashboard')  # <-- Use namespaced name here
    else:
        form = TurfForm()
    return render(request, 'owner/add_turf.html', {'form': form})
