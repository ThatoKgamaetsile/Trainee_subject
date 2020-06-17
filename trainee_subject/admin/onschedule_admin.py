from django.contrib import admin

from ..admin_site import trainee_subject_admin
from ..models import OnSchedule
from .modeladmin_mixins import ModelAdminMixin


@admin.register(OnSchedule, site=trainee_subject_admin)
class OnScheduleAdmin(ModelAdminMixin, admin.ModelAdmin):

    instructions = None
    fields = (
        'subject_identifier', 'onschedule_datetime')

    list_display = ('subject_identifier', 'onschedule_datetime')

    list_filter = ('onschedule_datetime', )

    search_fields = ('subject_identifier', )

    def get_readonly_fields(self, request, obj=None):
        return ('subject_identifier', 'onschedule_datetime')
