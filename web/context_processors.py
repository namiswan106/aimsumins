from .models import Service



def main_context(request):
    service=Service.objects.all().order_by('-id')[:4]
    return {
        "footer_services": service,
    }