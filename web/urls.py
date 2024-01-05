from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("blogs/", views.BlogView.as_view(), name="blogs"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
]