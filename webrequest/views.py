from django.http import HttpResponse
from django.shortcuts import render

from django.core.files import File
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import TerminationReportRequest, TerminationReportResponse
from .scripts.termination_script import create_termination_report

from .models import TelegramReportRequest, TelegramReportResponse
from .scripts.telegram_channels_script import create_telegram_channels_report

import os, sys
import datetime

@login_required
def new_termination_report(request):
    allPreviousReports = TerminationReportResponse.objects.all().order_by('-modified')[:5]
    reportName = "Termination report"
    reportDescription = "Bring termination reports to single format."
    scriptModificationTime = datetime.datetime.fromtimestamp(os.path.getmtime(settings.BASE_DIR + "/webrequest/scripts/termination_script.py")).strftime('%B %d, %Y')
    requestUrl = "/webrequest/termination/new/"
    processorUrl = "/webrequest/termination/make/"
    dropzoneMaxFiles = 2
    return render(request, 'request_report.html', {'reportsHistory': allPreviousReports, 'reportName': reportName, 'reportDescription': reportDescription, 'scriptModificationTime' : scriptModificationTime, 'processorUrl': processorUrl, 'dropzoneMaxFiles': dropzoneMaxFiles})

@login_required
def make_termination_report(request):
    reportRequest = TerminationReportRequest.objects.create(document1=request.FILES.get('file[0]'), document2=request.FILES.get('file[1]'))
    reportRequest.save()

    reportFilePath = create_termination_report([reportRequest.document1.path, reportRequest.document2.path])

    reportResponse = TerminationReportResponse(request=reportRequest)
    reportResponse.report.save(os.path.basename(reportFilePath), File(open(reportFilePath, "rb")))
    reportResponse.save()
    os.remove(reportFilePath)
    request.session['reportUrl'] = reportResponse.report.url
    return HttpResponse(reportResponse.report.url)

@login_required
def new_telegram_report(request):
    allPreviousReports = TelegramReportResponse.objects.all().order_by('-modified')[:5]
    reportName = "Telegram report"
    reportDescription = "Merge 4 databases of Telegram channels."
    scriptModificationTime = datetime.datetime.fromtimestamp(os.path.getmtime(settings.BASE_DIR + "/webrequest/scripts/telegram_channels_script.py")).strftime('%B %d, %Y')
    requestUrl = "/webrequest/telegram/new/"
    processorUrl = "/webrequest/telegram/make/"
    dropzoneMaxFiles = 4
    return render(request, 'request_report.html', {'reportsHistory': allPreviousReports, 'reportName': reportName, 'reportDescription': reportDescription, 'scriptModificationTime' : scriptModificationTime, 'processorUrl': processorUrl, 'dropzoneMaxFiles': dropzoneMaxFiles})

@login_required
def make_telegram_report(request):
    reportRequest = TelegramReportRequest.objects.create(document1=request.FILES.get('file[0]'), document2=request.FILES.get('file[1]'), document3=request.FILES.get('file[2]'), document4=request.FILES.get('file[3]'))
    reportRequest.save()

    reportFilePath = create_telegram_channels_report([reportRequest.document1.path, reportRequest.document2.path, reportRequest.document3.path, reportRequest.document4.path])

    reportResponse = TelegramReportResponse(request=reportRequest)
    reportResponse.report.save(os.path.basename(reportFilePath), File(open(reportFilePath, "rb")))
    reportResponse.save()
    os.remove(reportFilePath)
    request.session['reportUrl'] = reportResponse.report.url
    return HttpResponse(reportResponse.report.url)
