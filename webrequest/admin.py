from django.contrib import admin
from .models import Report, Request, Response

class ReportAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'description', 'maxDocuments', 'pathToScript', 'timeCreated', 'timeModified')

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
