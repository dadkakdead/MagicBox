from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='termination/new/')),

    path('termination/', RedirectView.as_view(url='new/')),
    path('termination/new/', views.new_termination_report, name='new_termination_report'),
    path('termination/make/', views.make_termination_report, name='make_termination_report'),

    path('telegram/', RedirectView.as_view(url='new/')),
    path('telegram/new/', views.new_telegram_report, name='new_telegram_report'),
    path('telegram/make/', views.make_telegram_report, name='make_telegram_report')
]
