from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from products.models import Books, Category


# Create your views here.

def home(request):
    books = Books.objects.filter(is_active=True)
    category = Category.objects.all()
    return render(request, 'home.html', {'books': books, 'category': category})

class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        super().get_context_data()



def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')
