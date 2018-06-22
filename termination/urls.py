from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_report, name='new_report'),
    path('download/', views.download_report, name="download_report")
]
