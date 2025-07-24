from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing(request):
    return render(request, 'landing.html')

@login_required
def role_redirect(request):
    user = request.user
    if getattr(user, 'user_type', None) == 'owner':
        return redirect('owner:owner_dashboard')
    elif getattr(user, 'user_type', None) == 'player':
        return redirect('players:player_home')
    else:
        return render(request, 'landing.html')
