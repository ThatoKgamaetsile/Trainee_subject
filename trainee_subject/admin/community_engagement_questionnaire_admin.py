from django.contrib import admin

from ..admin_site import trainee_subject_admin
from ..forms import CommunityEngagementQuestionnaireForm
from ..models import CommunityEngagementQuestionnaire


@admin.register(CommunityEngagementQuestionnaire, site=trainee_subject_admin)
class CommunityEngagementQuestionnaireAdmin(admin.ModelAdmin):

    form = CommunityEngagementQuestionnaireForm

    fields = (
        "active_in_community_activities",
        "local_government_election",
        "major_problems",
        "major_problems_other",
        "do_adults_work_together")

    radio_fields = {
        "active_in_community_activities": admin.VERTICAL,
        "local_government_election": admin.VERTICAL,
        "do_adults_work_together": admin.VERTICAL,
    }

    filter_horizontal = ("major_problems",)



