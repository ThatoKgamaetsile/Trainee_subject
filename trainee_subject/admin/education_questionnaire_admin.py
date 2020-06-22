from django.contrib import admin

from ..admin_site import trainee_subject_admin
from ..forms import EducationQuestionnaireForm
from ..models import EducationQuestionnaire


@admin.register(EducationQuestionnaire, site=trainee_subject_admin)
class EducationQuestionnaireAdmin(admin.ModelAdmin):

    form = EducationQuestionnaireForm

    radio_fields = {
        "work_status": admin.VERTICAL,
        "work_type": admin.VERTICAL,
        "recent_job": admin.VERTICAL,
        "previous_earning": admin.VERTICAL,
    }





