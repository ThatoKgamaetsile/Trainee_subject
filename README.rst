=====
TraineeProject
=====

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "traiee" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'trainee',
]

2. Include the trainee URLconf in your project urls.py like this::

path('trainee/', include('trainee')),

3. Run ``python manage.py migrate`` to create the trainee models.

4. Start the development server and visit http://127.0.0.1:8000/admin/

5. Visit http://127.0.0.1:8000/trainee/ to participate in the poll.
