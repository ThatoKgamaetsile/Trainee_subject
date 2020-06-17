from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from edc_base.constants import DEFAULT_BASE_FIELDS
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.sites import CurrentSiteManager
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_consent.field_mixins import (SampleCollectionFieldsMixin,
                                      CitizenFieldsMixin)
from edc_consent.field_mixins import IdentityFieldsMixin
from edc_consent.field_mixins import ReviewFieldsMixin, PersonalFieldsMixin
from edc_consent.field_mixins import VulnerabilityFieldsMixin
from edc_consent.managers import ConsentManager as SubjectConsentManager
from edc_consent.model_mixins import ConsentModelMixin
from edc_constants.choices import GENDER
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierModelMixin
from edc_registration.model_mixins import (
    UpdatesOrCreatesRegistrationModelMixin
    as BaseUpdatesOrCreatesRegistrationModelMixin)
from edc_search.model_mixins import SearchSlugManager

from ..subject_identifier import SubjectIdentifier
from .model_mixins import SearchSlugModelMixin


class ConsentManager(SubjectConsentManager, SearchSlugManager):

    def get_by_natural_key(self, subject_identifier, version):
        return self.get(
            subject_identifier=subject_identifier, version=version)


class UpdatesOrCreatesRegistrationModelMixin(
        BaseUpdatesOrCreatesRegistrationModelMixin):

    @property
    def registration_unique_field(self):
        return 'subject_identifier'

    @property
    def registration_options(self):
        """Gathers values for common attributes between the
        registration model and this instance.
        """
        registration_options = {}
        for field in self.registration_model._meta.get_fields():
            if (field.name not in DEFAULT_BASE_FIELDS + ['_state']
                    + [self.registration_unique_field]):
                try:
                    registration_options.update({field.name: getattr(
                        self, field.name)})
                except AttributeError:
                    pass
        return registration_options

    def registration_raise_on_not_unique(self):
        """Asserts the field specified for update_or_create is unique.
        """
        unique_fields = ['registration_identifier']
        for f in self.registration_model._meta.get_fields():
            try:
                if f.unique:
                    unique_fields.append(f.name)
            except AttributeError:
                pass
        if self.registration_unique_field not in unique_fields:
            raise ImproperlyConfigured(
                'Field is not unique. Got {}.{} -- {}'.format(
                    self._meta.label_lower, self.registration_unique_field))

    class Meta:
        abstract = True


MARITAL = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
)

CURRENTLY_LIVE_WITH = (
    ('alone', 'Alone'),
    ('partner_or_spouse', 'Partner or spouse'),
    ('siblings', 'Siblings'),
    ('other', 'Other'),
    ('do_not_want_to_answer', 'Do not want to answer'),
)


class SubjectConsent(
        ConsentModelMixin, SiteModelMixin,
        UpdatesOrCreatesRegistrationModelMixin,
        NonUniqueSubjectIdentifierModelMixin,
        IdentityFieldsMixin, ReviewFieldsMixin, PersonalFieldsMixin,
        SampleCollectionFieldsMixin, CitizenFieldsMixin,
        VulnerabilityFieldsMixin, SearchSlugModelMixin, BaseUuidModel):
    """ A model completed by the user that captures the ICF.
    """

    subject_screening_model = 'trainee_subject.subjectscreening'

    screening_identifier = models.CharField(
        verbose_name='Screening identifier',
        null=True,
        blank=True,
        max_length=50)

    gender = models.CharField(
        verbose_name="Gender",
        choices=GENDER,
        max_length=1,
        null=True,
        blank=False)

    marital_status = models.CharField(
        verbose_name='What is your marital status? ',
        max_length=10,
        choices=MARITAL)

    wives_husband_have = models.CharField(
        verbose_name=('WOMEN: How many wives does your '
                      'husband have (including traditional '
                      'marriage), including yourself? '),
        max_length=50)

    men_how_many_wives = models.CharField(
        verbose_name='MEN: How many wives do you have, including '
                     'traditional marriage? ',
        max_length=50)

    live_with = models.CharField(
        verbose_name='Who do you currently live with? ',
        max_length=50,
        choices=CURRENTLY_LIVE_WITH)

    is_signed = models.BooleanField(default=False, editable=False)

    consent = SubjectConsentManager()

    objects = ConsentManager()

    history = HistoricalRecords()

    on_site = CurrentSiteManager()

    def __str__(self):
        return f'{self.subject_identifier}'

    def save(self, *args, **kwargs):
        self.subject_type = 'subject'
        super().save(*args, **kwargs)

    def get_search_slug_fields(self):
        fields = super().get_search_slug_fields()
        fields.extend(['identity', 'screening_identifier',
                       'first_name', 'last_name'])
        return fields

    def make_new_identifier(self):
        """Returns a new and unique identifier.

        Override this if needed.
        """
        subject_identifier = SubjectIdentifier(
            identifier_type='subject',
            requesting_model=self._meta.label_lower,
            site=self.site)
        return subject_identifier.identifier

    @property
    def schedule_name(self):
        """Return a visit schedule name.
        """
        return 'schedule'

    class Meta(ConsentModelMixin.Meta):
        app_label = 'trainee_subject'
        get_latest_by = 'consent_datetime'
        unique_together = (('subject_identifier', 'version'),
                           ('first_name', 'dob', 'initials', 'version'))
        ordering = ('-created',)










