from django.db import models
import django.utils.timezone
from django.core.validators import MinValueValidator, RegexValidator
from django.conf import settings

import os
import shutil

class Report(models.Model):
    key = models.CharField(validators=[RegexValidator(regex='^[0-9a-zA-Z]{5,}$', message='Key should be at least 5 characters long', code='nomatch')], max_length=20)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    pathToScript = models.CharField(max_length=500, editable=False)
    maxDocuments = models.IntegerField(default=-1, validators=[MinValueValidator(-1)])
    allowedExtentions = models.CharField(default="XLS,XLSX,XLSM", validators=[RegexValidator(regex='^[,A-Z]{1,}$', message='Write the extension in upper case one by one. Example: XLS,XLSX,XLSM', code='nomatch')], max_length=100)
    timeCreated = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    timeModified = models.DateTimeField(default=django.utils.timezone.now, editable=False)

    @property
    def url(self):
        return "/webrequest/" + self.key + "/new"

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.timeCreated = django.utils.timezone.now()
            self.pathToScript = settings.BASE_DIR + "/webrequest/scripts/" + self.key + "_script.py"

        if os.path.isfile(self.pathToScript):
            pass
        else:
            source = settings.BASE_DIR + "/webrequest/scripts/backup/template_script.py"
            destination = self.pathToScript
            shutil.copy(source, destination)

        self.timeModified = django.utils.timezone.now()

        return super(Report, self).save(*args, **kwargs)

class Request(models.Model):
    report = models.ForeignKey(Report, blank=True, null=True, on_delete=models.CASCADE)
    requestZip = models.FileField(upload_to = 'requests/')
    timeCreated = models.DateTimeField(default=django.utils.timezone.now, editable=False)

    @property
    def key(self):
        return self.report.key

class Response(models.Model):
    request = models.ForeignKey(Request, blank=True, null=True, on_delete=models.CASCADE)
    responseFile = models.FileField(upload_to = 'responses/')
    timeCreated = models.DateTimeField(default=django.utils.timezone.now, editable=False)

    @property
    def key(self):
        return self.request.report.key
