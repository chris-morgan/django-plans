Information for developers
==========================

Source code
-----------

The source code for django-plans is `on GitHub`_. It is provided under the
MIT license (see ``MIT-LICENSE.TXT`` for the full text of the license).

Issues are tracked in the GitHub project's `issue tracker`_.

.. _on GitHub: https://github.com/cypreess/django-plans
.. _issue tracker: https://github.com/cypreess/django-plans/issues

.. highlight:: bash

If you're interested in helping out with django-plans, there are a few things
you may need.

First of all, you will of course need django-plans checked out (substitute the
clone line as appropriate)::

    $ git clone git://github.com/cypreess/django-plans.git
    $ cd django-plans

Note that as you're intending to develop it, you should ensure that all the
extra requirements (of the ``eu``, ``i18n`` and ``test`` features) are
installed. (Tasks like running all the tests and building the documentation
won't run correctly without them.) All of the necessary dependencies are
covered in the ``dev`` feature. Install it thus::

    $ pip install -e .\[dev]

(The backslash in ``\[`` is to ensure it works in ``zsh``; other \*nix shells
effectively ignore it.)

You can then do things like build the documentation::

    $ cd docs/
    $ make html
