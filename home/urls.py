from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('handel/',views.HandelFileUpload.as_view())
]