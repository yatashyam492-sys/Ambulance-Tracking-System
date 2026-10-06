from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import AmbulanceForm, BookingForm
from .models import Ambulance, Booking


def home(request):
    return render(request, "home.html")


def register_ambulance(request):
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ambulance_list')
    else:
        form = AmbulanceForm()

    return render(request, 'register_ambulance.html', {'form': form})


def ambulance_list(request):
    query = request.GET.get('q')

    if query:
        ambulances = Ambulance.objects.filter(
            ambulance_number__icontains=query
        )
    else:
        ambulances = Ambulance.objects.all()

    return render(request, 'ambulance_list.html', {
        'ambulances': ambulances
    })


def edit_ambulance(request, id):
    ambulance = Ambulance.objects.get(id=id)

    if request.method == 'POST':
        form = AmbulanceForm(request.POST, instance=ambulance)
        if form.is_valid():
            form.save()
            return redirect('ambulance_list')
    else:
        form = AmbulanceForm(instance=ambulance)

    return render(request, 'register_ambulance.html', {'form': form})


def delete_ambulance(request, id):
    ambulance = Ambulance.objects.get(id=id)
    ambulance.delete()
    return redirect('ambulance_list')
@login_required
def dashboard(request):
    total = Ambulance.objects.count()
    available = Ambulance.objects.filter(status="Available").count()
    busy = Ambulance.objects.filter(status="Busy").count()

    context = {
        'total': total,
        'available': available,
        'busy': busy,
    }

    return render(request, 'dashboard.html', context)

def book_ambulance(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookingForm()

    return render(request, 'book_ambulance.html', {'form': form})

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import get_object_or_404
from .models import Booking


@login_required
def booking_history(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_history.html', {
        'bookings': bookings
    })


@login_required
def view_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'view_booking.html', {
        'booking': booking
    })


@login_required
def update_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_history')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'book_ambulance.html', {
        'form': form
    })


@login_required
def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()
    return redirect('booking_history')