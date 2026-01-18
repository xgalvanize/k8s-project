# utils/pdf.py
from io import BytesIO
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML

def generate_pdf(template_src, context_dict={}):
    html_string = render_to_string(template_src, context_dict)
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    return response
