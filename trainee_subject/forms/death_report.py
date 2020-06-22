from ..models import DeathReport
from .form_mixins import SubjectModelFormMixin


class DeathReportForm (SubjectModelFormMixin):

    class Meta:
        model = DeathReport
        fields = '__all__'
