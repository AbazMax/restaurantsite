from django.shortcuts import render, HttpResponse, redirect
from main.models import UserReservation, UserMessage

# Create your views here.
def reservations_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    return render(request, 'reservations_list.html', context={
        'lst': lst,
    })

def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservations_list')

def message_list(request):
    mes_list = UserMessage.objects.filter(is_processed=False)
    return render(request, 'message_list.html', context={
        'mes_list': mes_list,
    })

def update_message(request, pk):
    UserMessage.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:message_list')