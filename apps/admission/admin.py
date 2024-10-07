from django.contrib import admin

from apps.admission.models import AdmissionProcess


@admin.register(AdmissionProcess)
class AdmissionProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'subtitle', 'short_name_admin', 'short_name_display', 'application_target_type', 'display_in_public_school_directory')
    search_fields = ('name', )
    list_filter = ('application_target_type',)
