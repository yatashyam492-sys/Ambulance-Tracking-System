from django import forms
from .models import Ambulance, Booking

class AmbulanceForm(forms.ModelForm):
    class Meta:
        model = Ambulance
        fields = '__all__'

        widgets = {
            'ambulance_number': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control'}),
            'driver_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'current_location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'