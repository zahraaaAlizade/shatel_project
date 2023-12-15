from django.urls import reverse_lazy
from rest_framework import viewsets
from .forms import UserRegisterForm
from .models import User
from .serializers import UserSerializer
from django.views.generic import TemplateView
import pandas as pd
import io
from django.shortcuts import render
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserViewList(generic.ListView):
    queryset = User.objects.all()
    template_name = 'read_csv.html'
    context_object_name = 'users'


class CsvUploader(TemplateView):
    template_name = 'csv_uploader.html'

    def post(self, request):
        context = {
            'messages': []
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
            try:
                User.objects.create(
                    username=record['username'],
                    email=record['email'],
                    national_id=record['national_id'],
                    password=record['password'],
                )
            except Exception as e:
                context['exceptions_raised'] = e

        return render(request, self.template_name, context)


