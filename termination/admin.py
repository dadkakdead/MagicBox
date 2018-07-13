from django.contrib import admin
from .models import TerminationReportRequest, TerminationReportResponse

# Register your models here.
class TerminationReportRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'document1', 'document2', 'created','modified')
    readonly_fields = ('created', 'id',)

class TerminationReportResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'request', 'report', 'created','modified')
    readonly_fields = ('created', 'id',)

admin.site.register(TerminationReportRequest, TerminationReportRequestAdmin)
admin.site.register(TerminationReportResponse, TerminationReportResponseAdmin)
