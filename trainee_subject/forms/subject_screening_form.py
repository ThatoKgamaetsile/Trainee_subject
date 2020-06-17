from django import forms

from ..models import SubjectScreening


class SubjectModelFormMixin(forms.ModelForm):

    pass


class SubjectScreeningForm(SubjectModelFormMixin):

    class Meta:
        model = SubjectScreening
        fields = '__all__'
