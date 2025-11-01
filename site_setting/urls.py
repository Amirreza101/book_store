from django.urls import path
from . import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('contact/',views.contact_view,name='contact'),
    path('about-us/',views.about,name='about-us'),
    path('<error>',views.not_found,name='404'),
]