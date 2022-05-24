from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin

# Register your models here.

class SearchAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ("term", "meaning","href",)

admin.site.register(Search, SearchAdmin)

class AnalyticsAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Analytics, AnalyticsAdmin)

class AnthropometryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Anthropometry, AnthropometryAdmin)

class ComputerAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Computer, ComputerAdmin)

class CostAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Distribution, CostAdmin)

class HumanAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Human, HumanAdmin)

class ManagementAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Management, ManagementAdmin)
class ManufacturingAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Manufacturing, ManufacturingAdmin)

class new_OperationsAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(new_Operations, new_OperationsAdmin)

class QualityAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

admin.site.register(Quality, QualityAdmin)