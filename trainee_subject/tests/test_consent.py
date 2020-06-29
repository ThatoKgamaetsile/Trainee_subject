import re

from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import UUID_PATTERN, YES
from edc_facility.import_holidays import import_holidays
from edc_registration.models import RegisteredSubject
from model_mommy import mommy

from ..models import SubjectConsent, OnSchedule


class TestSubjectConsent(TestCase):

    def setUp(self):
        import_holidays()

    def test_allocated_subject_identifier(self):
        """Test consent successfully allocates subject identifier on
        save.
        """
        options = {
            'consent_datetime': get_utcnow,
            'version': '1'}
        mommy.make_recipe('trainee_subject.subjectconsent', **options)
        print(SubjectConsent.objects.all()[0].subject_identifier)
        self.assertFalse(
            re.match(
                UUID_PATTERN,
                SubjectConsent.objects.all()[0].subject_identifier))

    def test_consent_creates_registered_subject(self):
        options = {
            'consent_datetime': get_utcnow,
            'version': '1'}
        self.assertEquals(RegisteredSubject.objects.all().count(), 0)
        mommy.make_recipe('trainee_subject.subjectconsent', **options)
        self.assertEquals(RegisteredSubject.objects.all().count(), 1)

    def test_onschedule_created_on_consent(self):
        subject_consent = mommy.make_recipe(
            'trainee_subject.subjectconsent',
            consent_datetime=get_utcnow,
            version='1')
        options = {
            'subject_identifier': subject_consent.subject_identifier,
            'citizen_or_not': YES,
            'enrollment_site': 'gaborone_private_hospital'}
        mommy.make_recipe(
            'trainee_subject.subjectscreening', **options)

        try:
            OnSchedule.objects.get(
                subject_identifier=subject_consent.subject_identifier)
        except ObjectDoesNotExist:
            self.fail('ObjectDoesNotExist was unexpectedly raised.')
