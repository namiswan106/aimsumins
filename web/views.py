from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

# Create your views here.

class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["is_index"] = True
        return context
    

class AboutView(TemplateView):
    template_name = "web/about.html"

class ContactView(TemplateView):
    template_name = "web/contact.html"

class ServicesView(TemplateView):
    template_name = "web/services.html"

class BlogView(TemplateView):
    template_name = "web/blog.html"

class PortfolioView(TemplateView):
    template_name = "web/portfolio.html"