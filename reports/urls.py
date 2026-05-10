from django.urls import path
from . import views
urlpatterns = [
    path('dashboard/', views.reports_home, name='reports_home'),
    path('pdf/', views.generate_pdf_report, name='report_pdf'),
    path('excel/', views.generate_excel_report, name='report_excel'),
]
