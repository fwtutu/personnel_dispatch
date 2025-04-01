from django.urls import path
from .views import customer_home, customer_profile, book_care_service, cancel_appointment  

urlpatterns = [
    path('home/', customer_home, name='customer_home'),
    path('customer_profile/', customer_profile, name='customer_profile'),
    path('book_care_service/', book_care_service, name='book_care_service'),
    path('cancel_appointment/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
]
