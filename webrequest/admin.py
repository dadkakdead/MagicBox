from django.contrib import admin
from django import forms
from .models import Report, Request, Response


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def clean(self):
        maxDocuments = self.cleaned_data.get('maxDocuments')
        if maxDocuments < -1 or maxDocuments == 0:
            raise forms.ValidationError("MaxDocuments can equal either a positive number or -1.")
        return self.cleaned_data

class ReportAdmin(admin.ModelAdmin):
    form = ReportForm

    list_display = ('key', 'name', 'description', 'maxDocuments', 'allowedExtentions', 'pathToScript', 'timeCreated', 'timeModified')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['key', 'pathToScript']
        else:
            return []

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'timeCreated', 'key', 'requestZip')
    readonly_fields = ('timeCreated', 'id')

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id',  'timeCreated', 'key', 'request', 'responseFile')
    readonly_fields = ('timeCreated', 'id')

admin.site.register(Report, ReportAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(Response, ResponseAdmin)
