from django.urls import path
from .views import reservations_list, update_reservation, message_list, update_message

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservations_list, name='reservations_list'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reserve'),
    path('messages/', message_list, name='message_list'),
    path('messages/update/<int:pk>', update_message, name='update_message')
]