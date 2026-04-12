from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name = 'inbox'),
    path('sent/', views.sent_messages, name = 'sent_messages'),
    path('drafts/', views.drafts, name = 'drafts'),
    path('compose/', views.compose, name = 'compose'),
    path('reply/<int:reply_to>/', views.compose, name = 'reply_message'),
    path('<int:pk>/', views.view_message, name = 'view_message'), 
    path('<int:pk>/delete/', views.delete_message, name = 'delete_message'),
]