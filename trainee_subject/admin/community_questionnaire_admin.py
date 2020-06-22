from django.contrib import admin

from ..admin_site import trainee_subject_admin
from ..forms import CommunityQuestionnaireForm
from ..models import CommunityQuestionnaire


@admin.register(CommunityQuestionnaire, site=trainee_subject_admin)
class CommunityQuestionnaireAdmin(admin.ModelAdmin):

    form = CommunityQuestionnaireForm

    fields = (
        "community_activities",
        "election",
        "problems",
        "problems_other",
        "collaboration")

    radio_fields = {
        "community_activities": admin.VERTICAL,
        "election": admin.VERTICAL,
        "collaboration": admin.VERTICAL,
    }

    filter_horizontal = ("problems",)



