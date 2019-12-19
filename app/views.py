from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import Restaurant
from .models import Reservation
from .models import ContactUs
from django.urls import reverse

# For creating CRUD for contacts
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Reverse-Lazy function - redirects urls based on their name
from django.urls import reverse_lazy

# Import messages (From partials) to show success/warning messages in the page
from django.contrib import messages

from django.core.mail import send_mail
from foodfun.settings import EMAIL_HOST_USER

# Create your views here.
# def home(request):
#    context = {}
#   return render(request, "index.html", context)


class HomePageView(ListView):
    template_name = "index.html"
    model = Restaurant
    context_object_name = "latest_restaurant_list"

    # Get list of all contacts only for logged-in user
    def get_queryset(self):
        restaurants = super().get_queryset()
        return restaurants


class AboutPageView(ListView):
    template_name = "about.html"
    model = Restaurant
    context_object_name = "latest_restaurant_list"


class MenuPageView(ListView):
    template_name = "menu.html"
    model = Restaurant
    context_object_name = "menu_details"


class ContactPageView(ListView):
    template_name = "contact.html"
    model = Restaurant
    context_object_name = "menu_details"


class RestaurantView(DetailView):
    template_name = 'dishes.html'
    model = Restaurant
    context_object_name = 'restaurant_detail'

    def get_context_data(self, **kwargs):
        context = super(RestaurantView, self).get_context_data(**kwargs)
        # context['RATING_CHOICES'] = Review.RATING_CHOICES
        return context


class RestaurantReservationForm(DetailView):
    template_name = 'create_reservation.html'
    model = Restaurant
    context_object_name = 'restaurant_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['RATING_CHOICES'] = Review.RATING_CHOICES
        return context


def createReservation(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    new_review = Reservation(
        booking_for_date=request.POST['booking_for_date'],
        guests=request.POST['guests'],
        time=request.POST['time'],
        booked_name=request.POST['booked_name'],
        booked_email=request.POST['booked_email'],
        booked_phone=request.POST['booked_phone'],
        restaurant=restaurant)
    new_review.save()

    # Sending Email through Gmail SMTP
    subject = 'MyRestaurants - Reservation Confirmed'
    message = 'Dear '+request.POST['booked_name']
    message += '\n Your reservation is confirmed for the restaurant '+restaurant.name
    message += '\n Please go through below details:'
    message += '\n Name:'+request.POST['booked_name']
    message += '\n Email:'+request.POST['booked_email']
    message += '\n Phone:'+request.POST['booked_phone']
    message += '\n No.of Guests:'+request.POST['guests']
    message += '\n Time Slot:'+request.POST['time']
    recepient = request.POST['booked_email']+'hrs'
    send_mail(subject,
              message, EMAIL_HOST_USER, [recepient], fail_silently=False)

    messages.success(
        request, 'Your reservation has been saved successfully')
    return HttpResponseRedirect(reverse('dishes', args=(restaurant.id,)))


def contactEmail(request):
    new_review = ContactUs(
        name=request.POST['name'],
        subject=request.POST['subject'],
        email=request.POST['email'],
        message=request.POST['message'],
    )
    new_review.save()

    messages.success(
        request, 'Email sent successfully, We will contact you soon.')
    return HttpResponseRedirect(reverse('contact'))
