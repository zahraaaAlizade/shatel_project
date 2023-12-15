from django.urls import path,include
from rest_framework import routers
from mainApp.views import UserViewSet, CsvUploader, UserViewList, SignUpView
from django.urls import re_path as url

router = routers.DefaultRouter()

#API
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('api/', include(router.urls), name='api'),
    path('users/', UserViewList.as_view()),
    url('^csv-uploader/$', CsvUploader.as_view(), name='csv-uploader'),
]