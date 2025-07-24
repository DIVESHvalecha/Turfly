from django.shortcuts import render, get_object_or_404
from owner.models import Turf, Booking
from django.db.models import Q
from datetime import date, time

# Player homepage view

def player_home(request):
    turfs = Turf.objects.all()
    location = request.GET.get('location')
    min_price = request.GET.get('min_price') or request.GET.get('price_min')
    max_price = request.GET.get('max_price') or request.GET.get('price_max')
    amenities = request.GET.get('amenities')
    date_str = request.GET.get('date')
    min_rating = request.GET.get('min_rating')

    if location:
        turfs = turfs.filter(location__icontains=location)
    if min_price:
        turfs = turfs.filter(price_per_hour__gte=min_price)
    if max_price:
        turfs = turfs.filter(price_per_hour__lte=max_price)
    if amenities:
        for amenity in amenities.split(','):
            turfs = turfs.filter(amenities__icontains=amenity.strip())
    if date_str:
        booked_turf_ids = Booking.objects.filter(date=date_str).values_list('turf_id', flat=True)
        turfs = turfs.exclude(id__in=booked_turf_ids)
    if min_rating:
        turfs = turfs.filter(rating__gte=min_rating)

    # Determine current month and year for the calendar header
    if date_str:
        current_date = date.fromisoformat(date_str)
    else:
        current_date = date.today()
    current_month = current_date.strftime('%B')
    current_year = current_date.year

    context = {
        'turfs': turfs,
        'selected_location': location or '',
        'selected_min_price': min_price or '',
        'selected_max_price': max_price or '',
        'selected_amenities': amenities or '',
        'selected_date': date_str or '',
        'selected_min_rating': min_rating or '0',
        'current_month': current_month,
        'current_year': current_year,
    }
    return render(request, 'players/player_home.html', context)


def normalize_slot(slot):
    # Converts '09:00-10:00' or '9:00-10:00' to '9:00-10:00' for comparison
    try:
        start, end = slot.split('-')
        start = time.fromisoformat(start.strip()).strftime('%-H:%M')
        end = time.fromisoformat(end.strip()).strftime('%-H:%M')
        return f"{start}-{end}"
    except Exception:
        return slot.strip()

def turf_detail(request, turf_id):
    turf = get_object_or_404(Turf, id=turf_id)
    selected_date = request.GET.get('date') or date.today().isoformat()
    # Parse available time slots
    all_slots = [slot.strip() for slot in (turf.available_time_slots or '').split(',') if slot.strip()]
    # Normalize all slots for comparison
    normalized_all_slots = [normalize_slot(slot) for slot in all_slots]
    # Get booked slots for the selected date
    booked = Booking.objects.filter(turf=turf, date=selected_date).values_list('start_time', 'end_time')
    booked_slots = [f"{s.strftime('%-H:%M')}-{e.strftime('%-H:%M')}" for s, e in booked]
    # Filter out booked slots
    available_slots = [slot for slot, norm_slot in zip(all_slots, normalized_all_slots) if norm_slot not in booked_slots]
    return render(request, 'players/turf_detail.html', {
        'turf': turf,
        'available_slots': available_slots,
        'selected_date': selected_date,
    })
