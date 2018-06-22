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

class TerminationReportRequestForm(forms.ModelForm):
    def clean(self):
        doc1 = self.cleaned_data.get("document1", False)
        #doc1_extension = magic.from_buffer(doc1.read())
        doc1_name, doc1_extension = os.path.splitext(str(doc1))

        doc2 = self.cleaned_data.get("document2", False)
        #doc2_extension = magic.from_buffer(doc2.read())
        doc2_name, doc2_extension = os.path.splitext(str(doc2))

        if not ".xls" in doc1_extension or not ".xls" in doc2_extension:
            raise forms.ValidationError("File type not similar to -> Microsoft Excel <- . 1:" + doc1_extension + ", 2:" + doc2_extension)

    class Meta:
        model = TerminationReportRequest
        fields = ('document1', 'document2')

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
