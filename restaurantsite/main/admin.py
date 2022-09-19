from django.contrib import admin
from .models import Category, Dish, UserReservation, Events, Gallery, Chefs, Testimonials, TopSitePresentation,\
    About, WhyUs, Titles, OurInformation, UserMessage
# Register your models here.
admin.site.register(Category)
admin.site.register(UserReservation)
admin.site.register(Events)
admin.site.register(Gallery)
admin.site.register(Chefs)
admin.site.register(Testimonials)
admin.site.register(TopSitePresentation)
admin.site.register(About)
admin.site.register(WhyUs)
admin.site.register(Titles)
admin.site.register(OurInformation)
admin.site.register(UserMessage)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('name',), }