from django.db import models
from edc_constants.choices import YES_NO
# from .model_mixins import CrfModelMixin


WORK_TYPE = (
    ('occasional_or_casual_employment_piece_job',
     'Occasional or Casual employment (piece job)'),
    ('seasonal_employment', 'Seasonal employment'),
    ('foal_wage_employment_full_time', 'Foal wage employment (full-time)rm'),
    ('formal_wage_employment_part_time', 'Formal wage employment (part-time)'),
    ('self_employed_in_agriculture', 'Self-employed in agriculture'),
    ('self_employed_making_money_full_time',
     'Self-employed making money, full time'),
    ('self_employed_making_money_part_time',
     'Self-employed making money, part time'),
    ("dont_want_to_answer", "Don't want to answer"),
    ('other', 'Other'),
)

WORK_TYPE_RECENT = (
    ('farmer_own_land', 'Farmer (own land)'),
    ('farm_work_on_employers_land', 'Farm work on employers land'),
    ('domestic_worker', 'Domestic worker'),
    ('work_in_bar_hotel_guest_house_entertainment_venue',
     'Work in bar/ hotel/ guest house/ entertainment venue'),
    ('fishing', 'Fishing'),
    ('mining', 'Mining'),
    ('tourism', 'Tourism/game parks'),
    ('working_in_shop_small_business', 'Working in shop / small business'),
    ('informal_selling', 'Informal selling'),
    ('commercial_sex_worker', 'Commercial sex work'),
    ('transport_trucker_taxi_driver', 'Transport (trucker/ taxi driver)'),
    ('factory_worker', 'Factory worker'),
    ('guard_security_company', 'Guard (security company)'),
    ('police_soldier', 'Police/ Soldier'),
    ('clerical_and_office_worker', 'Clerical and office work'),
    ('government_worker', 'Government worker'),
    ('teacher', 'Teacher'),
    ('health_care_worker', 'Health care worker'),
    ('other_professional', 'Other professional'),
    ("dont_want_to_answer", "Don't want to answer"),
    ('other', '"Other'),
)

MONEY_EARNED = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('1_199_pula', '1-199 pula'),
    ('200_499_pula', '200-499 pula'),
    ('500_999_pula', '500-999 pula'),
    ('1000_4999_pula', '1000-4999 pula'),
    ('5000_10_000_pula', '5000-10,000 pula'),
    ('more_than_10_000_pula', 'More than 10,000 pula'),
    ('dont_want_to_answer', "Don't want to answer"),
)


class EducationQuestionnaire(models.Model):

    currently_working = models.CharField(
        verbose_name='Are you currently working ',
        max_length=10,
        choices=YES_NO)

    what_type_of_work = models.CharField(
        verbose_name='In your main job what type of work do you do? ',
        max_length=50,
        choices=WORK_TYPE)

    recent_job = models.CharField(
        verbose_name='Describe the work that you do or did in your most'
                     ' recent job. If you have more than one profession, '
                     'choose the one you spend the most time doing. ',
        max_length=50,
        choices=WORK_TYPE)

    money_you_earned = models.CharField(
        verbose_name='In the past month, how much money did you '
                     'earn from work you did or received in payment? ',
        max_length=50,
        choices=MONEY_EARNED)













