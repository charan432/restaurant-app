from django.contrib import admin

# Register your models here.
from app.models import *


# Register your models here.
# To use import/export feature in admin panel
from import_export.admin import ImportExportModelAdmin


class RestaurantAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'city')


class DishAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price', 'description')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking_for_date', 'time', 'guests', 'booked_name',
                    'booked_email', 'booked_phone', 'booked_date', 'restaurant_id')


class ContactUsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message', 'email_date')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
