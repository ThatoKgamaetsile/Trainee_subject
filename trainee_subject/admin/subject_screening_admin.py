from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from edc_base.sites.admin import ModelAdminSiteMixin
from edc_model_admin import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    ModelAdminRedirectOnDeleteMixin)
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)
from edc_metadata import NextFormGetter

from ..admin_site import trainee_subject_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin,
                      ModelAdminRedirectOnDeleteMixin,
                      ModelAdminSiteMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'
    next_form_getter_cls = NextFormGetter


@admin.register(SubjectScreening, site=trainee_subject_admin)
class SubjectScreeningAdmin(admin.ModelAdmin):

    form = SubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'gender',
                'citizen_or_not',
                'married_to_motswana',
                'literate_or_illiterate',
                'literate_witness',
                'minor_or_not')}),
        ('Review Questions', {
            'fields': (
                'marriage_certificate_proof',),
            'description': 'The following questions are directed '
                           'to the interviewer.'}),
        audit_fieldset_tuple)

    search_fields = ('screening_identifier',)

    radio_fields = {
        "gender": admin.VERTICAL,
        "citizen_or_not": admin.VERTICAL,
        "married_to_motswana": admin.VERTICAL,
        "literate_or_illiterate": admin.VERTICAL,
        "literate_witness": admin.VERTICAL,
        "minor_or_not": admin.VERTICAL,
        "marriage_certificate_proof": admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)

