from django import forms

from ..models import SubjectScreening


class SubjectModelFormMixin(forms.ModelForm):

    pass


class SubjectScreeningForm(SubjectModelFormMixin):

    screening_identifier = forms.CharField(
        required=False,
        label='Screening Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = SubjectScreening
        fields = '__all__'
