from django.contrib import admin
from .models import TerminationReportRequest, TerminationReportResponse
from .models import TelegramReportRequest, TelegramReportResponse

class TerminationReportRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'document1', 'document2', 'modified')
    readonly_fields = ('created', 'id',)

class TerminationReportResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'request', 'report', 'modified')
    readonly_fields = ('created', 'id',)

admin.site.register(TerminationReportRequest, TerminationReportRequestAdmin)
admin.site.register(TerminationReportResponse, TerminationReportResponseAdmin)

class TelegramReportRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'document1', 'document2', 'document3', 'document4', 'modified')
    readonly_fields = ('created', 'id',)

class TelegramReportResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'request', 'report', 'modified')
    readonly_fields = ('created', 'id',)

admin.site.register(TelegramReportRequest, TelegramReportRequestAdmin)
admin.site.register(TelegramReportResponse, TelegramReportResponseAdmin)
