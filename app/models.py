from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=20, default="")
    zipCode = models.CharField(max_length=20, blank=True, null=True)
    stateOrProvince = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to='images/', blank=True)

    def __unicode__(self):
        return u"%s" % self.name


# To get average rating of a restaurant in restaurant details page
def averageRating(self):
    reviewCount = self.restaurantreview_set.count()
    if not reviewCount:
        return 0
    else:
        ratingSum = sum([float(review.rating)
                         for review in self.restaurantreview_set.all()])
        return ratingSum / reviewCount


class Dish(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(
        'USD', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="project1", blank=True, null=True)
    restaurant = models.ForeignKey(
        Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __unicode(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})


class Reservation(models.Model):
    booking_for_date = models.CharField(max_length=150)
    time = models.CharField(max_length=50)
    guests = models.CharField(max_length=10)
    booked_name = models.CharField(max_length=100)
    booked_email = models.CharField(max_length=200)
    booked_phone = models.CharField(max_length=100)
    booked_date = models.DateField(default=date.today)
    restaurant = models.ForeignKey(
        Restaurant, null=True, related_name='reservation', on_delete=models.CASCADE)

    def __unicode(self):
        return u"%s" % self.restaurant


class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    email_date = models.DateField(default=date.today)

    def __unicode(self):
        return u"%s" % self.name
