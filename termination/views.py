from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import TerminationReportRequest, TerminationReportResponse, TerminationReportRequestForm

from .utils import create_termination_report
from django.core.files import File
import os, sys
from django.template import loader

from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

def new_report(request):
    if request.method == 'POST':
        form = TerminationReportRequestForm(request.POST, request.FILES)
        if form.is_valid():
            reportRequest = form.save()

            reportPath = create_termination_report([reportRequest.document1.path, reportRequest.document2.path])

            reportInstance = TerminationReportResponse(request=reportRequest)
            reportInstance.report.save(os.path.basename(reportPath), File(open(reportPath, "rb")))
            reportInstance.save()
            os.remove(reportPath)
            request.session['reportUrl'] = reportInstance.report.url
            return redirect('download_report')
    else:
        form = TerminationReportRequestForm()
    return render(request, 'request_report.html', {'form': form})

def download_report(request):
    if request.session['reportUrl'] != "":
        reportUrl = request.session['reportUrl']
        request.session['reportUrl'] = ""
        return render(request, 'download_report.html', {'reportUrl': reportUrl})
    else:
        return HttpResponse("Empty request. Please start from <a href='/termination/new'>request form</a>")
