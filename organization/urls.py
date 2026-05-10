from django.urls import path
from . import views

urlpatterns = [
    path('', views.department_list, name='department_list'),
    path('<int:pk>/', views.department_detail, name='department_detail'),
    path('teamtype/<int:pk>/', views.teamtype_detail, name='teamtype_detail'),
    path('org-chart/', views.org_chart, name='org_chart'),
    path('dependencies/', views.dependency_graph, name='dependency_graph'),
]
