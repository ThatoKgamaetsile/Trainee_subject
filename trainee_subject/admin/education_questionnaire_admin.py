from django.contrib import admin

from ..admin_site import trainee_subject_admin
from ..forms import EducationQuestionnaireForm
from ..models import EducationQuestionnaire


@admin.register(EducationQuestionnaire, site=trainee_subject_admin)
class EducationQuestionnaireAdmin(admin.ModelAdmin):

    form = EducationQuestionnaireForm

    radio_fields = {
        "currently_working": admin.VERTICAL,
        "what_type_of_work": admin.VERTICAL,
        "recent_job": admin.VERTICAL,
        "money_you_earned": admin.VERTICAL,
    }





