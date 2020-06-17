from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin



from ..admin_site import trainee_subject_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening
from edc_model_admin import audit_fieldset_tuple, audit_fields


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

