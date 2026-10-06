from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Ambulance
    path('register/', views.register_ambulance, name='register'),
    path('list/', views.ambulance_list, name='ambulance_list'),
    path('edit/<int:id>/', views.edit_ambulance, name='edit_ambulance'),
    path('delete/<int:id>/', views.delete_ambulance, name='delete_ambulance'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Booking
    path('book/', views.book_ambulance, name='book_ambulance'),
    path('booking-history/', views.booking_history, name='booking_history'),
    path('booking/view/<int:id>/', views.view_booking, name='view_booking'),
    path('booking/update/<int:id>/', views.update_booking, name='update_booking'),
    path('booking/delete/<int:id>/', views.delete_booking, name='delete_booking'),

    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]