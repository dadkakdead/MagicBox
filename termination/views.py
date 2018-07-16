from django.http import HttpResponse
from django.shortcuts import render

from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import TerminationReportRequest, TerminationReportResponse
from .scripts.termination_script import create_termination_report

import os, sys
import datetime



@login_required
def new_report(request):
    allPreviousReports = TerminationReportResponse.objects.all().order_by('-modified')[:5]
    scriptModificationTime = datetime.datetime.fromtimestamp(os.path.getmtime(settings.BASE_DIR + "/termination/scripts/termination_script.py")).strftime('%B %d, %Y')
    reportName = "Termination report"
    processorUrl = "/termination/make/"
    return render(request, 'request_report.html', {'reportsHistory': allPreviousReports, 'reportName': reportName, 'scriptModificationTime' : scriptModificationTime, 'processorUrl': processorUrl})

@login_required
def make_report(request):
    reportRequest = TerminationReportRequest.objects.create(document1=request.FILES.get('file[0]'), document2=request.FILES.get('file[1]'))
    reportRequest.save()

    reportFilePath = create_termination_report([reportRequest.document1.path, reportRequest.document2.path])

    reportResponse = TerminationReportResponse(request=reportRequest)
    reportResponse.report.save(os.path.basename(reportFilePath), File(open(reportFilePath, "rb")))
    reportResponse.save()
    os.remove(reportFilePath)
    request.session['reportUrl'] = reportResponse.report.url
    return HttpResponse(reportResponse.report.url)
