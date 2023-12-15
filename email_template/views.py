from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from .models import EmailTemplate
from .serializers import EmailSerializer
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm


class EmailTemplateListCreateView(generics.ListCreateAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailSerializer


class EmailTemplateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailSerializer


def send_email(request):
    if request.method == 'POST':
        forms = EmailForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            subject = forms.cleaned_data['subject']
            body = forms.cleaned_data['body']

            email_template = EmailTemplate.objects.get(name=name)

            final_subject = email_template.subject.format(subject=subject)
            final_body = email_template.body.format(body=body)

            send_mail(final_subject, final_body, settings.DEFAULT_FROM_EMAIL, [name])
            return JsonResponse({'message': 'Email sent successfully'})
    else:
        forms = EmailForm()
    return render(request, 'email_template.html', {'form': forms})
