from django.urls import path
from . import views
from django.views.generic import DetailView, ListView

urlpatterns = [
    # Routing for function based view
    # path('', views.home, name="home"),
    path('', views.HomePageView.as_view(), name="home"),
    path('about', views.AboutPageView.as_view(), name="about"),
    path('dishes/<int:pk>', views.RestaurantView.as_view(), name="dishes"),
    path('menu', views.MenuPageView.as_view(), name="menu"),
    path('contact', views.ContactPageView.as_view(), name="contact"),
    path('reservation/<int:pk>', views.RestaurantReservationForm.as_view(),
         name="reservation_form"),
    path('reservation/create/<int:pk>',
         views.createReservation, name='create_reservation'),
    path('contactus',
         views.contactEmail, name='send_email'),
]
