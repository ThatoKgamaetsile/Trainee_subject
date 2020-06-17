from edc_locator.action_items import SubjectLocatorAction as BaseSubjectLocatorAction

from edc_action_item import site_action_items


SUBJECT_LOCATOR_ACTION = 'submit-trainee-subject-locator'


class TraineeSubjectLocatorAction(BaseSubjectLocatorAction):
    name = SUBJECT_LOCATOR_ACTION
    display_name = 'Submit Subject Locator'
    reference_model = 'trainee_subject.subjectlocator'
    admin_site_name = 'trainee_subject_admin'


site_action_items.register(TraineeSubjectLocatorAction)
