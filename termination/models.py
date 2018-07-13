from django.db import models
from django import forms
from django.forms.widgets import HiddenInput
import magic
import uuid
# Create your models here.

import os
from django.utils import timezone

from django.conf import settings
from django.core.files.storage import FileSystemStorage

class TerminationReportRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document1 = models.FileField(upload_to = 'requests/')
    document2 = models.FileField(upload_to = 'requests/')
    created = models.DateTimeField(default=timezone.now(), editable=False)
    modified = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TerminationReportRequest, self).save(*args, **kwargs)

class TerminationReportResponse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request = models.ForeignKey(TerminationReportRequest, blank=True, null=True, on_delete=models.CASCADE)
    report = models.FileField(upload_to = 'responses/')
    created = models.DateTimeField(default=timezone.now(), editable=False)
    modified = models.DateTimeField(default=timezone.now())

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(TerminationReportResponse, self).save(*args, **kwargs)
