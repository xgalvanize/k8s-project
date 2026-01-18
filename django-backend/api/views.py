from django.utils.timezone import now
from django.shortcuts import render
from .utils.pdf import generate_pdf

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})

def health_page(request):
    return render(request, 'api/health.html')

def pdf_report(request):
    context = {
        "title": "My PDF Report",
        "date": now(),
        "items": [
            {"name": "Apples", "qty": 10},
            {"name": "Oranges", "qty": 5},
        ],
    }
    return generate_pdf("api/report.html", context)
