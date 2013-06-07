Installation
============

Installing module code
------------------------

You can install app using package manager directly from github:

.. code-block:: bash

    $ pip install -e git://github.com/cypreess/django-plans.git#egg=django-plans

If you want the EU feature dependencies installed or i18n support, use this:

.. code-block:: bash

    $ pip install -e git://github.com/cypreess/django-plans.git#egg=django-plans\[eu,i18n]

(The backslash in ``\[`` is to ensure it works in ``zsh``; other \*nix shells
effectively ignore it.)

For integration instruction please see section  :doc:`integration`.



Running example project
-----------------------

Clone git repository to your current directory:

.. code-block:: bash

    $ git clone git://github.com/cypreess/django-plans.git


Optionally create virtual env and get required packages to run example project:

.. code-block:: bash

    $ cd django-plans/example
    $ pip install -r pip_example.req


Initialize example project database:

.. code-block:: bash

    $ cd ..
    $ python manage.py syncdb

Load an initial data (used also for testing):

.. code-block:: bash

    $ python manage.py loaddata test_django-plans_auth test_django-plans_plans


Start dev webserver:

.. code-block:: bash

    $ python manage.py runserver
