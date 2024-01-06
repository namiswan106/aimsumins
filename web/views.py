from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# models
from .models import Service, Blog,PortfolioCategory,Portfolio,Client_logo
from .forms import ContactForm


# Create your views here.

class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["is_index"] = True
        context["services"] = Service.objects.all()
        context["blogs"] = Blog.objects.all()
        context["client_logos"] = Client_logo.objects.all()
        return context
    

class AboutView(TemplateView):
    template_name = "web/about.html"
    

class ContactView(FormView):
    form_class = ContactForm
    template_name='web/contact.html'

    def form_valid(self, form):
        form.save()
        response_data = { "status": "true","title": "Successfully Submitted","message": "Message successfully updated",}
        return JsonResponse(response_data)

    def form_invalid(self, form):
        response_data = {"status": "false","title": "Form validation error",}
        return JsonResponse(response_data, status=400)
    

class ServicesView(ListView):
    model = Service
    template_name = "web/services.html"
    
    
class ServicesDetailView(DetailView):
    model = Service
    template_name = "web/service-detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_service = self.get_object()

        # Exclude the current service from the list of services
        context["services"] = Service.objects.exclude(pk=current_service.pk)

        return context
    

class BlogView(ListView):
    model = Blog
    template_name = "web/blog.html"
    
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "web/blog-detail.html"
    

class PortfolioView(ListView):
    model = Portfolio
    template_name = "web/portfolio.html"
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = PortfolioCategory.objects.all()
        return context
    