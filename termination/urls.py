from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='new/')),
    path('new/', views.new_report, name='new_report'),
    path('make/', views.make_report, name='make_report')
]
