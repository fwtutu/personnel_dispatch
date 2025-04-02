from django.urls import path
from .views import customer_home, customer_profile, book_care_service, cancel_appointment  
from . import views

urlpatterns = [
    path('home/', customer_home, name='customer_home'),
    path('customer_profile/', customer_profile, name='customer_profile'),
    path('book_care_service/', book_care_service, name='book_care_service'),
    path('cancel_appointment/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    
    #long_term_care說明
    path('long_term_care/', views.long_term_care_home, name='long_term_care_home'),
    path('long_term_care/about/', views.long_term_care_about, name='long_term_care_about'),
    path('long_term_care/services/', views.long_term_care_services, name='long_term_care_services'),
    path('long_term_care/application/', views.long_term_care_application, name='long_term_care_application'),
    path('long_term_care/contact/', views.long_term_care_contact, name='long_term_care_contact'),
]
