from django.http import HttpResponse
from django.shortcuts import render

from django.core.files import File
from django.core.files.base import ContentFile

from django.contrib.auth.decorators import login_required

from .models import Report, Request, Response
from django.conf import settings

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
            allPreviousResponses =  Response.objects.all().order_by('-timeCreated')
            responsesPerKey  = []
            for response in allPreviousResponses:
                if response.key == reportKey:
                    responsesPerKey.append(response)

            # pass report settings to front-end
            scriptPath = settings.BASE_DIR + reportMatched[0].pathToScript
            if pathlib.Path(scriptPath).is_file():
                scriptModificationTime = str(datetime.datetime.fromtimestamp(os.path.getmtime(scriptPath)).strftime('%B %d, %Y'))
            else:
                scriptModificationTime = str()

            requestUrl = "/webrequest/" + reportKey + "/new/"

            processorUrl = "/webrequest/" + reportKey + "/make/"

            return render(request, 'request_report.html', {'report': reportMatched[0], 'allReports': reversed(Report.objects.all().order_by('-key')), 'responses': responsesPerKey[:5], 'scriptModificationTime' : scriptModificationTime, 'requestUrl': requestUrl, 'processorUrl': processorUrl})
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
    reportFilePath = processingScript(reportKey, reportRequest.requestZip.path)

    # save the resulting report in the response object
    reportResponse = Response(request=reportRequest)
    reportResponse.responseFile.save(os.path.basename(reportFilePath), File(open(reportFilePath, "rb")))
    reportResponse.save()

    # remove the temporary file
    os.remove(reportFilePath)

    # return the download link
    request.session['reportUrl'] = reportResponse.responseFile.url

    return HttpResponse(reportResponse.responseFile.url)

@login_required
def download_script(request, scriptName):
    scriptPath = settings.BASE_DIR + "/webrequest/scripts/" + scriptName
    if os.path.exists(scriptPath):
        with open(scriptPath, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="text/plain")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(scriptPath)
            return response
