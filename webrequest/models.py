from django.db import models
import django.utils.timezone
from django.core.validators import MinValueValidator
from django.conf import settings

class Report(models.Model):
    key = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    pathToScript = models.CharField(max_length=500, editable=False)
    maxDocuments = models.IntegerField(validators=[MinValueValidator(1)])
    timeCreated = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    timeModified = models.DateTimeField(default=django.utils.timezone.now, editable=False)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.timeCreated = django.utils.timezone.now()
            self.pathToScript = settings.BASE_DIR + "/webrequest/scripts/" + self.key + "_script.py"
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
