from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_constants.choices import YES_NO, GENDER
# from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_base.utils import get_utcnow
from edc_base.model_validators import eligible_if_yes
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.model_mixins import BaseModel
from edc_search.model_mixins import SearchSlugManager
from edc_search.model_mixins import SearchSlugModelMixin as Base

from ..eligibility import Eligibility
# from ..models.model_mixins import SearchSlugModelMixin
from ..screening_identifier import ScreeningIdentifier
# from ..choices import MINOR_OR_GROWN, ENROLLMENT_SITES


class SearchSlugModelMixin(Base):
    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.append('screening_identifier')
        return fields

    class Meta:
        abstract = True


class SubjectScreening(
        SiteModelMixin,
        SearchSlugModelMixin, BaseUuidModel):

    eligibility_cls = Eligibility
    identifier_cls = ScreeningIdentifier

    screening_identifier = models.CharField(
        verbose_name="Eligibility Identifier",
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        help_text='Date and time of report.',
        null=True)

    gender = models.CharField(
        choices=GENDER,
        max_length=10)

    citizen_or_not = models.CharField(
        verbose_name='Are you a Botswana citizen? ',
        max_length=10,
        choices=YES_NO,
        validators=[eligible_if_yes, ])

    married_to_motswana = models.CharField(
        verbose_name='If not a citizen, are you legally '
                     'married to a Botswana Citizen? ',
        max_length=10,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        help_text="( if 'NO' STOP patient cannot be enrolled )", )

    marriage_certificate_proof = models.CharField(
        verbose_name='[Interviewer] Has the participant '
                     'produced the marriage certificate, as proof? ',
        max_length=10,
        choices=YES_NO,
        help_text="( if 'NO' STOP patient cannot be enrolled )",
        validators=[eligible_if_yes, ])

    literate_or_illiterate = models.CharField(
        verbose_name='Is the participant LITERATE? ',
        max_length=50,
        choices=YES_NO,
        validators=[eligible_if_yes, ])

    literate_witness = models.CharField(
        verbose_name='If ILLITERATE, is there a LITERATE '
                     'witness available? ',
        max_length=50,
        choices=YES_NO,
        validators=[eligible_if_yes, ])

    minor_or_not = models.CharField(
        verbose_name='If minor, is there a guardian available? ',
        max_length=50,
        choices=YES_NO,
        validators=[eligible_if_yes, ])

    eligible = models.BooleanField(
        default=False,
        editable=False)

    def __str__(self):
        return f'{self.screening_identifier}'

    history = HistoricalRecords()

    class Meta:
        app_label = 'trainee_subject'
#        verbose_name = "Trainee Eligibility"
#        verbose_name_plural = "Trainee Eligibility"

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(
            trainee_status=self.citizen_or_not)
        self.eligible = eligibility_obj.eligible
        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

#    def get_search_slug_fields(self):
#        fields = super().get_search_slug_fields()
#        fields.append('screening_identifier')
#        return fields

