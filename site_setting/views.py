from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView

from products.models import Books, Category


# Create your views here.

def navbar_partial(request):
    return render(request,'includes/navbar.html')

def footer_partial(request):
    return render(request,'includes/footer.html')
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(is_active=True)
        return context


def contact(request):
    return render(request, 'pages/contact.html')


def about(request):
    return render(request, 'pages/about.html')

