from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

@login_required
def role_redirect(request):
    user = request.user
    if hasattr(user, 'is_owner') and user.is_owner:
        return redirect('owner:owner_dashboard')  # Replace with your owner's dashboard URL name
    else:
        return render(request, 'landing.html')  # Temporary fallback
        # return redirect('booking:page')  # Replace with your booking page URL name
