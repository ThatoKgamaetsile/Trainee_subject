from edc_constants.constants import OTHER, NONE, UNKNOWN
from edc_list_data import PreloadData


list_data = {
    'trainee_subject.problems': [
        ('hiv_aids', 'HIV/AIDS'),
        ('schools', 'Schools'),
        ('sewer', 'Sewer'),
        ('unemployment', 'Unemployment'),
        ('roads', 'Roads'),
        ('water', 'Water'),
        ('house', 'House'),
        ('malaria', 'Malaria'),
        ('not_applicable', 'Not Applicable'),
    ],
}

preload_data = PreloadData(
    list_data=list_data)
