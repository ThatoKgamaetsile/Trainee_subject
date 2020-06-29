from datetime import date

from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_constants.choices import YES, POS
from edc_constants.constants import NO
from edc_visit_tracking.constants import SCHEDULED
from faker import Faker
from faker.providers import BaseProvider
from model_mommy.recipe import Recipe, seq, related

from .models import DeathReport
from .models import SubjectVisit
from .models import SubjectConsent
from .models import SubjectScreening


class DateProvider(BaseProvider):

    def next_month(self):
        return (get_utcnow() + relativedelta(months=1)).date()

    def last_year(self):
        return (get_utcnow() - relativedelta(years=1)).date()

    def three_months_ago(self):
        return (get_utcnow() - relativedelta(months=3)).date()

    def thirty_four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=34)).date()

    def four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=4)).date()

    def yesterday(self):
        return (get_utcnow() - relativedelta(days=1)).date()


fake = Faker()
fake.add_provider(DateProvider)
# fake.add_provider(EdcConsentProvider)

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    consent_datetime=get_utcnow(),
    dob=get_utcnow() - relativedelta(years=25),
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials='XX',
    gender='M',
    identity=seq('12315678'),
    confirm_identity=seq('12315678'),
    identity_type='OMANG',
    is_dob_estimated='-',
    is_incarcerated=NO,)

subjectvisit = Recipe(
    SubjectVisit,
    reason=SCHEDULED,)


subjeclocator = Recipe(
    SubjectLocator,
    alt_contact_cell_number='72123721',
    has_alt_contact=NO,
    alt_contact_name='John Doe',
    alt_contact_rel='Sibling',
    alt_contact_cell='78298422',
    other_alt_contact_cell='71297390',
    alt_contact_tel='3178634',
    local_clinic='00-0-00',
    home_village='Oodi',)

deathreport = Recipe(
    DeathReport,
    death_date=get_utcnow() - relativedelta(weeks=1),
    primary_death_cause='Clinical record',
    death_cause_description='details here',
    death_cause_category='Cancer',
    diagnosis_code='details here',
    comments='details here',)


subjectscreening = Recipe(
    SubjectScreening,
    has_diagnosis=YES,
    enrollment_site='gaborone_private_hospital'
)

