from .list_models import Problems
from django.db import models
from edc_base.model_fields import OtherCharField
from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin
from ..choices import ACTIVENESS, DID_YOU_VOTE, NEIGHBORHOOD_PROBLEMS, ADULTS_WORK_TOGETHER


class CommunityEngagementQuestionnaire(CrfModelMixin):

    active_in_community_activities = models.CharField(
        verbose_name='How active are you in community activities? ',
        max_length=50,
        help_text='Such as burial society, Motshelo, Syndicate, PTA, '
                  'VDC(Village Development Committee), Mophato and'
                  ' development of the community that surrounds you? ',
        choices=ACTIVENESS)

    local_government_election = models.CharField(
        verbose_name='Did you vote in the last local government election? ',
        max_length=50,
        choices=DID_YOU_VOTE)

#    major_problems = MultiSelectField(
#        verbose_name='What are the major problems in this neighborhood? ',
#        choices=NEIGHBORHOOD_PROBLEMS)

    major_problems = models.ManyToManyField(
        Problems,
        verbose_name='What are the major problems in this neighborhood? ',
        max_length=20,
        blank=True,
        help_text='',
    )

    major_problems_other = OtherCharField()

    do_adults_work_together = models.CharField(
        blank=True,
        verbose_name='If there is a problem in this neighborhood, '
                     'do the adults work together in solving it? ',
        max_length=50,
        choices=ADULTS_WORK_TOGETHER)

    def __str__(self):
        return f'{self.screening_identifier}'
