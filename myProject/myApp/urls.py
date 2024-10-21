from . import views
from django.urls import path

urlpatterns = [
    path('base', views.base, name="base"),
    path('about/', views.about, name='about'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('contact/', views.contact, name='contact'),
    path('contact-form/', views.contact_form, name='contact_form'),
    path('gallery/', views.gallery, name='gallery'),
    path("", views.index, name='index'),
    path('organizer/', views.organizer, name='organizer'),
    path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('single-gallery/', views.single_gallery, name='single_gallery'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
]