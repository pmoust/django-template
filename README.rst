template
========

django template

Usage
-----

#. Create a new virtualenv and activate it

#. Install cookiecutter from git (need at least version 0.7. Pypi has 0.6.4)::

    pip install -e git+https://github.com/audreyr/cookiecutter.git@436390901f36dc3087ad12eff395b9396edc451f#egg=cookiecutter-master

#. Use cookiecutter and the cookiecutter-template to create a new django site::

    cookiecutter https://github.com/pmav99/django-template.git

#. Answer the questions.

#. Let's say that you named your project ``fataoulas`` and the domain name
   ``fataoulas.gr``. Install the dependencies and create the database (sqlite by
   default)::

   cd fataoulas
   pip install requirements/local.txt
   cd root
   python manage.py syncdb
   python manage.py migrate

#. Open a new terminal and create an email server::

    python -m smtpd -n -c DebuggingServer localhost:1025

#. Run Django's test server::

   python manage.py runserver

#. Enjoy!

