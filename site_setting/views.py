from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Books, Category
from .forms import ContactUsModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()



def navbar_partial(request):
    return render(request, 'includes/navbar.html')


def footer_partial(request):
    return render(request, 'includes/footer.html')


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.filter(is_active=True)
        return context


@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactUsModelForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.email = request.user
            contact.save()
            return redirect('home')
    else:
        form = ContactUsModelForm()
    return render(request, 'pages/contact.html', {'form': form})




class ContactUsView(LoginRequiredMixin, FormView):
    template_name = 'pages/contact.html'
    form_class = ContactUsModelForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.email = self.request.user
        contact.save()
        return super().form_valid(form)


def about(request):
    return render(request, 'pages/about.html')


def not_found(request, error):
    return render(request, 'pages/404.html', status=404)
