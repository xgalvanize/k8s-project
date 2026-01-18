from django.urls import path
from .views import health, health_page
from .views import pdf_report

urlpatterns = [
    path('health/', health),            # API JSON
    path('health-page/', health_page),  # HTML page
    path('report/pdf/', pdf_report, name="pdf_report"),
]
