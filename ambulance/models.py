from django.db import models

class Ambulance(models.Model):
    ambulance_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    driver_phone = models.CharField(max_length=15)
    current_location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.ambulance_number


class Booking(models.Model):
    patient_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=200)
    emergency_type = models.CharField(max_length=100)
    ambulance_type = models.CharField(max_length=50)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name