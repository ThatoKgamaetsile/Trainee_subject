from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Trainee Subject'
    site_header = 'Trainee Subject'
    index_title = 'Trainee Subject'
    site_url = '/trainee_subject/list/'


trainee_subject_admin = AdminSite(name='trainee_subject_admin')



