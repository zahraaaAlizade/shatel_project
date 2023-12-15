from django.urls import path
from .views import EmailTemplateListCreateView, EmailTemplateRetrieveUpdateDestroyView, send_email

urlpatterns = [
    path('email-templates/', EmailTemplateListCreateView.as_view(), name='email-template-list'),
    path('email-templates/', EmailTemplateRetrieveUpdateDestroyView.as_view(), name='email-template-detail'),
    path('send-email/', send_email, name='send_email'),
]
