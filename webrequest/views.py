from django.http import HttpResponse
from django.shortcuts import render

from django.core.files import File
from django.core.files.base import ContentFile

from django.contrib.auth.decorators import login_required

from .models import Report, Request, Response

import os, sys
import time, datetime

import io
import pathlib
import zipfile
import importlib

@login_required
def new_report(request, reportKey):
    #check if there is a report for given key
    reportMatched = Report.objects.all().filter(key=reportKey)
    reportMatchCounter = len(reportMatched)

    if reportMatchCounter > 1:
        return HttpResponse("The are " + str(reportMatchCounter) + " reports for the key ->" + reportKey + "<- but it should be 1. Please go to admin panel and fix this.")
    else:
        if reportMatchCounter == 1:
            # filter out the responses for given key
            allPreviousReports =  Response.objects.all().order_by('-timeCreated')[:5]
            somePreviousReports = []
            for previousReport in allPreviousReports:
                if previousReport.key == reportKey:
                    somePreviousReports.append(previousReport)

            # pass report settings to front-end
            reportName = reportMatched[0].name

            reportDescription = reportMatched[0].description

            if pathlib.Path(reportMatched[0].pathToScript).is_file():
                scriptModificationTime = str(datetime.datetime.fromtimestamp(os.path.getmtime(reportMatched[0].pathToScript)).strftime('%B %d, %Y'))
            else:
                scriptModificationTime = str()

            requestUrl = "/webrequest/" + reportKey + "/new/"

            processorUrl = "/webrequest/" + reportKey + "/make/"

            dropzoneMaxFiles = reportMatched[0].maxDocuments

            return render(request, 'request_report.html', {'reportsHistory': somePreviousReports, 'reportName': reportName, 'reportDescription': reportDescription, 'scriptModificationTime' : scriptModificationTime, 'processorUrl': processorUrl, 'dropzoneMaxFiles': dropzoneMaxFiles})
        else:
            return HttpResponse("There is no report for key ->" + reportKey + "<-. Please check the URL.")

@login_required
def make_report(request, reportKey):
    # read all input files as bytes stream, merge into single bytes object
    zipBuffer = io.BytesIO()
    with zipfile.ZipFile(zipBuffer, "a", zipfile.ZIP_DEFLATED, False) as zf:
        for fileId in request.FILES:
            fileName = request.FILES.get(fileId).name
            fileBytes = io.BytesIO(request.FILES.get(fileId).read()).getvalue()
            zf.writestr(fileName, fileBytes)

    zipName = reportKey + "_" + str(round(time.time(),0))[:-2] + ".zip"

    # save the request
    reportRequest = Request.objects.create()
    reportRequest.report = Report.objects.all().filter(key=reportKey)[0]
    reportRequest.requestZip = ContentFile(zipBuffer.getvalue(), name=zipName)
    reportRequest.save()

    # run the report script
    processingModule = importlib.import_module("webrequest.scripts." + reportKey + "_script", package=None)
    processingScript = getattr(processingModule, "create_report")
    reportFilePath = processingScript(reportRequest.requestZip.path)

    # save the resulting report in the response object
    reportResponse = Response(request=reportRequest)
    reportResponse.responseFile.save(os.path.basename(reportFilePath), File(open(reportFilePath, "rb")))
    reportResponse.save()

    # remove the temporary file
    os.remove(reportFilePath)

    # return the download link
    request.session['reportUrl'] = reportResponse.responseFile.url

    return HttpResponse(reportResponse.responseFile.url)
