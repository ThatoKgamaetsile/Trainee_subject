from django import forms

from ..models import CommunityEngagementQuestionnaire


class CommunityEngagementQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = CommunityEngagementQuestionnaire
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommunityEngagementQuestionnaireForm, self).__init__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(CommunityEngagementQuestionnaireForm, self).__init__(*args, **kwargs)

        self.fields['major_problems'].required = False











