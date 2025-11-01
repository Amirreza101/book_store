from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from products.models import Books, Category


# Create your views here.

class BooksDetail(DetailView):
    template_name = 'books/book_detail.html'
    model = Books

class BooksList(ListView):
    template_name = 'books/book_list.html'
    model = Books
    context_object_name = 'books'
    ordering = '-created'
    paginate_by = 6

