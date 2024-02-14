from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("service/<slug>/", views.ServicesDetailView.as_view(), name="service-detail"),
    path("blogs/", views.BlogView.as_view(), name="blogs"),
    path("blog/<slug>/", views.BlogDetailView.as_view(), name="blog-detail"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    
    path("job/", views.JobListView.as_view(), name="job"),
    path("job/<slug>/", views.JobDetailView.as_view(), name="job-detail"),
    
    path('hire_enquiry/', views.HireEnquiryView.as_view(), name="hire-enquiry"),
]