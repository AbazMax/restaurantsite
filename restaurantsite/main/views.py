from django.shortcuts import render, redirect
from .models import Category, Dish, Events, Gallery, Chefs, Testimonials, TopSitePresentation, About, \
    WhyUs, Titles, OurInformation
from .forms import UserReservationForm, UserMessageForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        reservation = UserReservationForm(request.POST)
        message = UserMessageForm(request.POST)
        if reservation.is_valid():
            reservation.save()
            return redirect('/')
        if message.is_valid():
            message.save()
            return redirect('/')

    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specials = Dish.objects.filter(special=True)
    reservation = UserReservationForm()
    events = Events.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    chefs = Chefs.objects.all()
    testimonials = Testimonials.objects.all()
    top_site_presentation = TopSitePresentation.objects.filter()
    about = About.objects.first()
    why_us = WhyUs.objects.first()
    titles = Titles.objects.first()
    inf = OurInformation.objects.first()
    message = UserMessageForm()

    data = {'categories': categories,
            'dishes': dishes,
            'specials': specials,
            'reservation_form': reservation,
            'events': events,
            'gallery': gallery,
            'chefs': chefs,
            'testimonials': testimonials,
            'top_site_presentation': top_site_presentation,
            'about': about,
            'why_us': why_us,
            'titles': titles,
            'inf': inf,
            'message_form': message,

            }

    return render(request, 'main.html', context=data)
