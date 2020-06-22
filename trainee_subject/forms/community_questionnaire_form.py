from django import forms

from ..models import CommunityQuestionnaire


class CommunityQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = CommunityQuestionnaire
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CommunityQuestionnaireForm, self).__init__(*args, **kwargs)

        self.fields['problems'].required = False











