from django.urls import path
from . import views
urlpatterns = [
    path('books/<slug:slug>',views.BooksDetail.as_view(),name='book-detail'),
    path('books/',views.BooksList.as_view(),name= 'book-list'),
]