from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='telegram/new/')),

    path('scripts/<str:scriptName>', views.download_script, name='download_script'),
    path('<str:reportKey>/', RedirectView.as_view(url='new/')),
    path('<str:reportKey>/new/', views.new_report, name='new_report'),
    path('<str:reportKey>/make/', views.make_report, name='make_report')
]
