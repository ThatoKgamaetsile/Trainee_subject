from django.db import models
from edc_constants.choices import YES_NO
from .model_mixins import CrfModelMixin
from ..choices import WORK_TYPE, WORK_TYPE_RECENT, MONEY_EARNED


class EducationQuestionnaire(CrfModelMixin):

    work_status = models.CharField(
        verbose_name='Are you currently working ',
        max_length=10,
        choices=YES_NO)

    work_type = models.CharField(
        verbose_name='In your main job what type of work do you do? ',
        max_length=50,
        choices=WORK_TYPE)

    recent_job = models.CharField(
        verbose_name='Describe the work that you do or did in your most'
                     ' recent job. If you have more than one profession, '
                     'choose the one you spend the most time doing. ',
        max_length=50,
        choices=WORK_TYPE)

    previous_earning = models.CharField(
        verbose_name='In the past month, how much money did you '
                     'earn from work you did or received in payment? ',
        max_length=50,
        choices=MONEY_EARNED)













